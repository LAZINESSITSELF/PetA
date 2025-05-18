import { createRouter, createWebHistory } from 'vue-router'
import Login from '../pages/Login.vue'
import Dashboard from '../pages/Dashboard.vue'
import UserManagement from '../pages/UserManagement.vue'
import CustomerManagement from '../pages/CustomerManagement.vue'
import PenitipanManagement from '../pages/PenitipanManagement.vue'
import { useAuthStore } from '../stores/auth'

const routes = [
    { path: '/login', component: Login },
    { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
    { path: '/users', component: UserManagement, meta: { requiresAuth: true, roles: ['owner'] } },
    { path: '/customers', component: CustomerManagement, meta: { requiresAuth: true } },
    { path: '/penitipan', component: PenitipanManagement, meta: { requiresAuth: true } }
]

const router = createRouter({ history: createWebHistory(), routes })
router.beforeEach((to, _, next) => {
    const auth = useAuthStore()
    if (to.meta.requiresAuth && !auth.token) return next('/login')
    if (to.meta.roles && !to.meta.roles.includes(auth.role)) return next('/dashboard')
    next()
})
export default router