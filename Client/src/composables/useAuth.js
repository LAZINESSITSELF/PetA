import { ref } from 'vue'
import router from '../router'
import axios from 'axios'

const token = ref(localStorage.getItem('token') || '')
const role = ref(localStorage.getItem('role') || '')

export function useAuth() {
    async function login(u, p) {
        const { data } = await axios.post('http://localhost:5000/auth/login', { username: u, password: p })
        token.value = data.access_token
        role.value = data.role
        localStorage.setItem('token', token.value)
        localStorage.setItem('role', role.value)
        router.push('/dashboard')
    }
    function logout() {
        localStorage.clear()
        token.value = ''
        role.value = ''
        router.push('/login')
    }
    return { token, role, login, logout }
}