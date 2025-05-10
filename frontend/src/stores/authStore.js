import { writable } from 'svelte/store';
import { browser } from '$app/environment';
import { auth } from '$lib/api';

// Initial state
const initialState = {
    user: null,
    isAuthenticated: false,
    isLoading: true
};

// Create the store
const createAuthStore = () => {
    const { subscribe, set, update } = writable(initialState);
    
    return {
        subscribe,
        
        // Initialize the store - check if user is logged in
        init: async () => {
            // Only run in browser
            if (!browser) return;
            
            // Check if we have a token
            const token = localStorage.getItem('token');
            if (!token) {
                update(state => ({ ...state, isLoading: false }));
                return;
            }
            
            try {
                // Get current user data
                const userData = await auth.getCurrentUser();
                
                set({
                    user: userData,
                    isAuthenticated: true,
                    isLoading: false
                });
            } catch (error) {
                // Clear invalid token
                localStorage.removeItem('token');
                
                set({
                    user: null,
                    isAuthenticated: false,
                    isLoading: false
                });
            }
        },
        
        // Login user
        login: async (credentials) => {
            try {
                update(state => ({ ...state, isLoading: true }));
                
                const response = await auth.login(credentials);
                
                // Store token
                localStorage.setItem('token', response.token);
                
                // Get user data
                const userData = await auth.getCurrentUser();
                
                set({
                    user: userData,
                    isAuthenticated: true,
                    isLoading: false
                });
                
                return { success: true };
            } catch (error) {
                update(state => ({ 
                    ...state, 
                    isLoading: false,
                    isAuthenticated: false,
                    user: null
                }));
                
                return { 
                    success: false, 
                    error: error.message || 'Login failed' 
                };
            }
        },
        
        // Register user
        register: async (userData) => {
            try {
                update(state => ({ ...state, isLoading: true }));
                
                await auth.register(userData);
                
                // After registration, log the user in
                const loginResult = await auth.login({
                    email: userData.email,
                    password: userData.password
                });
                
                // Store token
                localStorage.setItem('token', loginResult.token);
                
                // Get user data
                const currentUser = await auth.getCurrentUser();
                
                set({
                    user: currentUser,
                    isAuthenticated: true,
                    isLoading: false
                });
                
                return { success: true };
            } catch (error) {
                update(state => ({ ...state, isLoading: false }));
                
                return { 
                    success: false, 
                    error: error.message || 'Registration failed' 
                };
            }
        },
        
        // Logout user
        logout: () => {
            localStorage.removeItem('token');
            
            set({
                user: null,
                isAuthenticated: false,
                isLoading: false
            });
        }
    };
};

// Export the store
export const authStore = createAuthStore(); 