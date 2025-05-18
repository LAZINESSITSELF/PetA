<template>
    <AppLayout>
        <div class="p-6">
            <h2 class="text-2xl font-bold mb-4">Data Penitipan</h2>
            <form @submit.prevent="addPenitipan" class="grid grid-cols-2 gap-2 mb-4">
                <input v-model="form.nama_hewan" placeholder="Nama Hewan" class="p-2 border rounded" />
                <input v-model="form.jenis_hewan" placeholder="Jenis Hewan" class="p-2 border rounded" />
                <input v-model="form.customer_id" placeholder="Customer ID" class="p-2 border rounded" />
                <input v-model="form.tanggal_penitipan" placeholder="Tanggal Titip (YYYY-MM-DD)"
                    class="p-2 border rounded" />
                <input v-model="form.tanggal_pengambilan" placeholder="Tanggal Ambil (YYYY-MM-DD)"
                    class="p-2 border rounded" />
                <input v-model.number="form.durasi_penitipan" placeholder="Durasi (hari)" class="p-2 border rounded" />
                <input v-model.number="form.tarif" placeholder="Tarif per hari" class="p-2 border rounded" />
                <input v-model="form.catatan_khusus" placeholder="Catatan Khusus"
                    class="p-2 border rounded col-span-2" />
                <button class="bg-green-600 text-white px-4 py-2 rounded col-span-2">Simpan</button>
            </form>
            <ul>
                <li v-for="p in data" :key="p._id" class="border-b py-2">
                    <strong>{{ p.nama_hewan }}</strong> — {{ p.jenis_hewan }} — Rp {{ p.total_biaya }}
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
const data = ref([])
const form = ref({ nama_hewan: '', jenis_hewan: '', customer_id: '', tanggal_penitipan: '', tanggal_pengambilan: '', durasi_penitipan: 0, tarif: 0, catatan_khusus: '', status_penitipan: 'aktif' })
async function fetchData() { const r = await axios.get('http://localhost:5000/penitipan', { headers: { Authorization: `Bearer ${token.value}` } }); data.value = r.data }
async function addPenitipan() { await axios.post('http://localhost:5000/penitipan', form.value, { headers: { Authorization: `Bearer ${token.value}` } }); fetchData() }

onMounted(fetchData)
</script>