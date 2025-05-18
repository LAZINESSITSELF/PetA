<template>
    <div>
        <Navbar />
        <main class="bg-gray-50 min-h-screen">
            <slot />
        </main>
    </div>
</template>
<script setup>
import Navbar from '../components/Navbar.vue'
</script>