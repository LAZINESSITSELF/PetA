import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
    state: () => ({ token: localStorage.getItem('token') || '', role: localStorage.getItem('role') || '' }),
    actions: {
        async login(u, p) {
            const res = await axios.post('http://localhost:5000/auth/login', { username: u, password: p })
            this.token = res.data.access_token
            this.role = res.data.role
            localStorage.setItem('token', this.token)
            localStorage.setItem('role', this.role)
        },
        logout() { localStorage.clear(); this.token = ''; this.role = '' }
    }
})