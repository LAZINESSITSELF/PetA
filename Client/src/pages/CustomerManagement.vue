<template>
    <AppLayout>
        <div class="p-6">
            <h2 class="text-2xl font-bold mb-4">Data Customer</h2>
            <form @submit.prevent="addCustomer" class="mb-4 flex gap-2">
                <input v-model="name" placeholder="Nama" class="p-2 border rounded" />
                <input v-model="email" placeholder="Email" class="p-2 border rounded" />
                <button class="bg-blue-600 text-white px-4 py-2 rounded">Tambah</button>
            </form>
            <ul>
                <li v-for="c in customers" :key="c._id" class="border-b py-2">
                    {{ c.name }} ({{ c.email }})
                </li>
            </ul>
        </div>
    </AppLayout>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAuth } from '../composables/useAuth'
import AppLayout from '../layouts/AppLayout.vue'

const { token } = useAuth()
const customers = ref([]), name = ref(''), email = ref('')
async function fetchCustomers() { const r = await axios.get('http://localhost:5000/customer', { headers: { Authorization: `Bearer ${token.value}` } }); customers.value = r.data }
async function addCustomer() { await axios.post('http://localhost:5000/customer', { name: name.value, email: email.value }, { headers: { Authorization: `Bearer ${token.value}` } }); name.value = ''; email.value = ''; fetchCustomers() }
onMounted(fetchCustomers)
</script>