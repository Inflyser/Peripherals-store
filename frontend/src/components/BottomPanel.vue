<template>
  <div class="bottom-panel">
    <div class="container bottom-panel-container">
      <div class="bottom-panel-left">
        <h2 class="slogan">Give All You Need</h2>
      </div>
      <div class="bottom-panel-right">
        <div class="bottom-search">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Поиск товаров..."
            class="bottom-search-input"
            @keyup.enter="handleSearch"
          />
          <button @click="handleSearch" class="bottom-search-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits<{
  search: [query: string]
}>()

const searchQuery = ref('')

function handleSearch() {
  if (searchQuery.value.trim()) {
    emit('search', searchQuery.value.trim())
    searchQuery.value = ''
  }
}
</script>

<style scoped>
.bottom-panel {
  background: #e5e5e5;
  padding: 40px 0;
}

.bottom-panel-container {
  width: 90%;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
}

.bottom-panel-left {
  flex-shrink: 0;
}

.slogan {
  margin: 0;
  font-size: 24px;
  font-weight: 700;
  color: #333;
}

.bottom-panel-right {
  flex: 1;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.bottom-search {
  display: flex;
  align-items: center;
  background: white;
  border-radius: 12px;
  overflow: hidden;
  max-width: 400px;
  width: 100%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.bottom-search-input {
  flex: 1;
  padding: 12px 16px;
  border: none;
  outline: none;
  font-size: 16px;
  background: transparent;
}

.bottom-search-input::placeholder {
  color: #999;
}

.bottom-search-button {
  padding: 12px 16px;
  background: #000;
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.3s ease;
}

.bottom-search-button:hover {
  background: #333;
}

/* Адаптивность */
@media (max-width: 1024px) {
  .bottom-panel-container {
    flex-direction: column;
    gap: 20px;
  }

  .bottom-panel-left,
  .bottom-panel-right {
    width: 100%;
  }

  .bottom-panel-right {
    justify-content: center;
  }

  .bottom-search {
    max-width: 100%;
  }
}

@media (max-width: 768px) {
  .bottom-panel {
    padding: 30px 0;
  }

  .bottom-panel-container {
    width: 100%;
  }

  .slogan {
    font-size: 20px;
    text-align: center;
  }
}
</style>
