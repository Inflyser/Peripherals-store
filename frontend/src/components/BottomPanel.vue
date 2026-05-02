<template>
  <div class="bottom-panel">
    <div class="bottom-header">
      <div class="container bottom-header-container">
        <h2 class="slogan">Give All You Need</h2>
        <div class="bottom-header-right">
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
          <button class="action-btn" title="Профиль">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

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
.bottom-header {
  background: white;
  padding: 20px 0;
  border-top: 1px solid #eee;
  margin: 0 100px 0 100px;
  border-top-left-radius: 25px;
  border-top-right-radius: 25px;
}

.bottom-header-container {
  width: 80%;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.slogan {
  margin: 0;
  font-size: 24px;
  font-weight: 700;
  color: #000;
}

.bottom-header-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.bottom-header-right .bottom-search {
  display: flex;
  align-items: center;
  background: #eee;
  border-radius: 10px;
  overflow: hidden;
  max-width: 300px;
  width: 100%;
}

.bottom-header-right .bottom-search-input {
  flex: 1;
  padding: 10px 14px;
  border: none;
  outline: none;
  font-size: 14px;
  background: transparent;
}

.bottom-header-right .bottom-search-input::placeholder {
  color: #666;
}

.bottom-header-right .bottom-search-button {
  padding: 10px 14px;
  background: #000;
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.3s ease;
}

.bottom-header-right .action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: #eee;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  color: #000;
  transition: background 0.3s ease;
}

.bottom-header-right .action-btn:hover {
  background: #ddd;
}

.bottom-panel {
  background: url('@/assets/font.svg') center/cover no-repeat;
  padding: 550px 0px 0px 0px;
}

.bottom-header {
  background: white;
  padding: 20px 0;
  border-top: 1px solid #eee;
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
