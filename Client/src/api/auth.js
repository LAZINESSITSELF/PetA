import axios from 'axios'
const api = axios.create({ baseURL: 'http://localhost:5000' })

export function login(username, password) {
    return api.post('/auth/login', { username, password })
}

export function logout() {
    return api.post('/auth/logout')
}
