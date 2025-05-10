# Buddie Project AI Rules

## Code Generation

### Backend (Python)

- Always use type hints for parameters and return values
- Follow PEP 8 style guidelines
- Add docstrings to all functions, classes, and methods
- Use SQLModel patterns for database operations
- Implement proper error handling with FastAPI
- Use dependency injection for database sessions and auth
- Write code that passes mypy type checking

### Frontend (SvelteKit/TypeScript)

- Use TypeScript types for all variables and functions
- Create proper interfaces for component props
- Implement state management with Svelte stores
- Follow SvelteKit file-based routing conventions
- Use Tailwind utility classes for styling
- Implement responsive design patterns
- Add JSDoc comments to complex functions

## Common Patterns

### API Endpoints

```python
@router.get("/endpoint", response_model=ResponseSchema)
async def get_resource(
    param: type = Query(..., description="Parameter description"),
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """
    Endpoint description.

    Returns:
        ResponseSchema: Description of return value
    """
    # Implementation
    return result
```

### Svelte Components

```svelte
<script lang="ts">
  import { onMount } from 'svelte';
  import type { ComponentProps } from './types';

  export let prop1: string;
  export let prop2: number = 0;

  let localState: string = '';

  onMount(() => {
    // Setup code
  });

  function handleEvent() {
    // Event handler
  }
</script>

<div class="component-wrapper">
  <!-- Component template -->
</div>

<style>
  /* Component-specific styles if needed */
</style>
```

## Coding Rules

1. **Keep It Simple**: Prefer simple, readable solutions
2. **Type Safety**: Ensure all code is properly typed
3. **Error Handling**: Implement proper error handling
4. **Testing**: Consider how code will be tested
5. **Performance**: Be mindful of performance implications
6. **Security**: Follow security best practices
7. **Documentation**: Document complex logic
8. **Consistency**: Follow established project patterns

## Business Logic Guidelines

1. **Cannabis Product Data**:
   - Store strain types, THC/CBD percentages, and terpene profiles
   - Support various product types (flower, edibles, concentrates, etc.)
2. **User Recommendations**:
   - Base recommendations on user preferences and ratings
   - Consider product similarities based on chemical profiles
3. **Scraping Logic**:
   - Implement anti-detection measures
   - Normalize product data across different sources
4. **Ratings & Reviews**:
   - Store numerical ratings (1-5 stars)
   - Allow text reviews
   - Calculate average ratings per product
