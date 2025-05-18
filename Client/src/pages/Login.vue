<template>
    <GuestLayout>
        <form @submit.prevent="loginUser" class="bg-white p-8 rounded shadow w-80">
            <h2 class="text-2xl font-bold mb-6 text-center">Login</h2>
            <input v-model="username" placeholder="Username" class="w-full mb-4 p-2 border rounded" />
            <input v-model="password" type="password" placeholder="Password" class="w-full mb-6 p-2 border rounded" />
            <button type="submit" class="w-full py-2 rounded bg-blue-600 text-white">Masuk</button>
        </form>
    </GuestLayout>
</template>

<script setup>
import { ref } from 'vue'
import { useAuth } from '../composables/useAuth'
const { login } = useAuth()
const username = ref(''), password = ref('')
function loginUser() { login(username.value, password.value) }
</script>