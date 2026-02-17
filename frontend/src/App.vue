<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
    <nav class="bg-white shadow-lg">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <h1 class="text-2xl font-bold text-indigo-600">Vercel & Render</h1>
          </div>
          <div class="flex items-center space-x-4">
            <div v-if="backendStatus" class="flex items-center space-x-2">
              <span class="w-3 h-3 bg-green-500 rounded-full"></span>
              <span class="text-sm text-gray-600">Backend Online</span>
            </div>
            <div v-else class="flex items-center space-x-2">
              <span class="w-3 h-3 bg-red-500 rounded-full"></span>
              <span class="text-sm text-gray-600">Backend Offline</span>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <!-- Status Section -->
      <div class="bg-white rounded-lg shadow-xl p-8 mb-8">
        <h2 class="text-3xl font-bold text-gray-900 mb-4">Backend Status</h2>
        <div v-if="loading" class="text-gray-600">Loading...</div>
        <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4">
          <p class="text-red-900">Error: {{ error }}</p>
        </div>
        <div v-else-if="backendStatus" class="grid grid-cols-2 gap-4">
          <div class="bg-green-50 rounded-lg p-4">
            <p class="text-sm text-green-700 font-semibold">Status</p>
            <p class="text-lg text-green-900">{{ backendStatus.status }}</p>
          </div>
          <div class="bg-blue-50 rounded-lg p-4">
            <p class="text-sm text-blue-700 font-semibold">Engine</p>
            <p class="text-lg text-blue-900">{{ backendData.backend_engine }}</p>
          </div>
          <div class="col-span-2 bg-indigo-50 rounded-lg p-4">
            <p class="text-sm text-indigo-700 font-semibold">Message</p>
            <p class="text-indigo-900">{{ backendStatus.message }}</p>
          </div>
        </div>
      </div>

      <!-- Data from Backend Section -->
      <div class="bg-white rounded-lg shadow-xl p-8 mb-8">
        <h2 class="text-3xl font-bold text-gray-900 mb-6">Módulos del Proyecto</h2>
        <div v-if="backendData.items && backendData.items.length > 0" class="space-y-4">
          <div
            v-for="item in backendData.items"
            :key="item.id"
            class="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:border-indigo-300 transition"
          >
            <div class="flex items-center space-x-4">
              <span class="text-2xl font-bold text-indigo-600">{{ item.id }}</span>
              <div>
                <p class="font-semibold text-gray-900">{{ item.name }}</p>
              </div>
            </div>
            <span
              :class="{
                'px-3 py-1 rounded-full text-sm font-medium': true,
                'bg-green-100 text-green-800': item.status === 'Completado',
                'bg-blue-100 text-blue-800': item.status === 'En progreso',
                'bg-yellow-100 text-yellow-800': item.status === 'Pendiente'
              }"
            >
              {{ item.status }}
            </span>
          </div>
        </div>
      </div>

      <!-- Interactive Section -->
      <div class="bg-white rounded-lg shadow-xl p-8">
        <h2 class="text-3xl font-bold text-gray-900 mb-4">Interacción</h2>
        
        <div class="mb-8">
          <label class="block text-sm font-medium text-gray-700 mb-2">Enter your name:</label>
          <input
            v-model="name"
            type="text"
            placeholder="Your name here"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
          />
        </div>

        <div v-if="name" class="bg-indigo-50 border border-indigo-200 rounded-lg p-4 mb-8">
          <p class="text-indigo-900">Hello, <strong>{{ name }}</strong>! Welcome to Vue.js with Tailwind CSS.</p>
        </div>

        <button
          @click="count++"
          class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-6 rounded-lg transition duration-200"
        >
          Click Count: {{ count }}
        </button>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { apiService } from './services/api'

const count = ref(0)
const name = ref('')
const loading = ref(true)
const error = ref<string | null>(null)
const backendStatus = ref<any>(null)
const backendData = ref<any>({ items: [] })

onMounted(async () => {
  try {
    loading.value = true
    const [status, data] = await Promise.all([
      apiService.getStatus(),
      apiService.getData(),
    ])
    backendStatus.value = status
    backendData.value = data
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Error fetching data from backend'
    console.error('Error:', err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
/* Component-specific styles can go here */
</style>
