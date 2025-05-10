import logging
import random
import time
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

import requests
from requests.exceptions import RequestException
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('scraper')

class BaseScraper(ABC):
    """
    Base class for all scrapers. Implements common functionality.
    """
    def __init__(self, dispensary_name: str, base_url: str):
        self.dispensary_name = dispensary_name
        self.base_url = base_url
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        ]
    
    def get_random_user_agent(self) -> str:
        """Return a random user agent from the list."""
        return random.choice(self.user_agents)
    
    def get_with_retry(self, url: str, max_retries: int = 3) -> Optional[requests.Response]:
        """
        Make a GET request with retries and anti-detection measures.
        """
        headers = {'User-Agent': self.get_random_user_agent()}
        
        for attempt in range(max_retries):
            try:
                # Add random delay between requests
                time.sleep(random.uniform(1, 3))
                
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                return response
            except RequestException as e:
                logger.warning(f"Request failed (attempt {attempt+1}/{max_retries}): {str(e)}")
                if attempt == max_retries - 1:
                    logger.error(f"All retries failed for {url}")
                    return None
    
    def scrape_with_playwright(self, url: str) -> Optional[str]:
        """
        Scrape a page using Playwright for JavaScript-heavy sites.
        """
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(
                    user_agent=self.get_random_user_agent()
                )
                page = context.new_page()
                page.goto(url)
                
                # Wait for content to load - adjust selector as needed
                page.wait_for_selector('body', timeout=10000)
                
                # Allow time for dynamic content to load
                time.sleep(random.uniform(2, 4))
                
                content = page.content()
                browser.close()
                return content
        except Exception as e:
            logger.error(f"Playwright scraping failed: {str(e)}")
            return None
    
    @abstractmethod
    def scrape_products(self) -> List[Dict[str, Any]]:
        """
        Scrape products from the dispensary website.
        Must be implemented by each specific scraper.
        """
        pass 