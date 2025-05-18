<template>
    <AppLayout>
        <div class="p-6">
            <h2 class="text-2xl font-bold mb-4">Manajemen User</h2>
            <form @submit.prevent="addUser" class="mb-4 flex gap-2">
                <input v-model="username" placeholder="Username" class="p-2 border rounded" />
                <input v-model="password" type="password" placeholder="Password" class="p-2 border rounded" />
                <button class="bg-green-600 text-white px-4 py-2 rounded">Tambah</button>
            </form>
            <!-- <ul>
                <li v-for="u in users" :key="u._id" class="border-b py-2 flex justify-between">
                    <span>{{ u.username }} ({{ u.role }})</span>
                    <button @click="deleteUser(u._id)" class="text-red-600">Hapus</button>
                </li>
            </ul> -->
        </div>
    </AppLayout>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAuth } from '../composables/useAuth'
import AppLayout from '../layouts/AppLayout.vue'

const { token } = useAuth()
const users = ref([]), username = ref(''), password = ref('')
async function fetchUsers() {
    const r = await axios.get('http://localhost:5000/users', { headers: { Authorization: `Bearer ${token.value}` } })
    users.value = r.data
}
async function addUser() { await axios.post('http://localhost:5000/auth/signup', { username: username.value, password: password.value }, { headers: { Authorization: `Bearer ${token.value}` } }); username.value = ''; password.value = ''; fetchUsers() }
async function deleteUser(id) { await axios.delete(`http://localhost:5000/users/${id}`, { headers: { Authorization: `Bearer ${token.value}` } }); fetchUsers() }
onMounted(fetchUsers)
</script>