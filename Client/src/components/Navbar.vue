<template>
    <nav class="bg-gray-800 text-white px-4 py-3 flex justify-between">
        <div>🐾 Pet Boarding</div>
        <div class="flex gap-4">
            <RouterLink to="/dashboard">Dashboard</RouterLink>
            <RouterLink v-if="role === 'owner'" to="/users">Users</RouterLink>
            <RouterLink to="/customers">Customers</RouterLink>
            <RouterLink to="/penitipan">Penitipan</RouterLink>
            <button @click="logout">Logout</button>
        </div>
    </nav>
</template>

<script setup>
import { useAuth } from '../composables/useAuth'
import { computed } from 'vue'
const { role, logout } = useAuth()
</script>