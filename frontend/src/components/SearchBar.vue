<template>
  <div class="search-bar">
    <input
      v-model="searchQuery"
      type="text"
      placeholder="Поиск товаров..."
      class="search-input"
      @keyup.enter="performSearch"
    />
    <button @click="performSearch" class="search-button">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
    </button>
    <button v-if="searchQuery" @click="clearSearch" class="clear-button">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits<{
  search: [query: string]
  clear: []
}>()

const searchQuery = ref('')

function performSearch() {
  if (searchQuery.value.trim()) {
    emit('search', searchQuery.value.trim())
  }
}

function clearSearch() {
  searchQuery.value = ''
  emit('clear')
}
</script>

<style scoped>
.search-bar {
  display: flex;
  align-items: center;
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  overflow: hidden;
  transition: border-color 0.3s ease;
}

.search-bar:focus-within {
  border-color: #667eea;
}

.search-input {
  flex: 1;
  padding: 12px 16px;
  border: none;
  outline: none;
  font-size: 16px;
  background: transparent;
}

.search-input::placeholder {
  color: #999;
}

.search-button {
  padding: 12px 16px;
  background: #667eea;
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.3s ease;
}

.search-button:hover {
  background: #5568d3;
}

.clear-button {
  padding: 12px 8px;
  background: transparent;
  color: #999;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.3s ease;
}

.clear-button:hover {
  color: #666;
}
</style>
