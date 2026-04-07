<template>
  <header class="header">
    <div class="container header-container">
      <!-- Левая часть: лого и название бренда -->
      <div class="header-left">
        <div class="logo-wrapper">
          <svg class="logo-icon" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
            <path d="M2 17l10 5 10-5"></path>
            <path d="M2 12l10 5 10-5"></path>
          </svg>
          <h1 class="brand-name">Peripherals Store</h1>
        </div>
      </div>

      <!-- Центральная часть: навигация -->
      <nav class="header-center">
        <RouterLink to="/" class="nav-link">Beranda</RouterLink>
        <RouterLink to="/shop" class="nav-link">shop</RouterLink>
        <RouterLink to="/blog" class="nav-link">blog</RouterLink>
      </nav>

      <!-- Правая часть: поиск, корзина, профиль -->
      <div class="header-right">
        <button class="search-btn" @click="toggleSearch" title="Поиск">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </button>
        <div class="header-actions">
          <button class="action-btn cart-btn" title="Корзина">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="9" cy="21" r="1"></circle>
              <circle cx="20" cy="21" r="1"></circle>
              <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
            </svg>
            <span class="cart-count">0</span>
          </button>
          <button class="action-btn profile-btn" title="Профиль">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'

const emit = defineEmits<{
  search: [query: string]
}>()

function toggleSearch() {
  const query = prompt('Введите поисковый запрос:')
  if (query && query.trim()) {
    emit('search', query.trim())
  }
}
</script>

<style scoped>
.header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  padding: 12px 0;
  display: flex;
  justify-content: center;
}

.header-container {
  width: 90%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
}

.container {
  max-width: 100%;
  margin: 0;
  padding: 0 20px;
}

.header .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
}

/* Левая часть - лого и бренд */
.header-left {
  flex-shrink: 0;
}

.logo-wrapper {
  display: flex;
  align-items: center;
  gap: 16px;
}

.logo-icon {
  flex-shrink: 0;
  color: #333;
}

.brand-name {
  margin: 0;
  font-size: 24px;
  font-weight: 700;
  color: #333;
  white-space: nowrap;
}

/* Центральная часть - навигация */
.header-center {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 50px;
}

.nav-link {
  color: #333;
  text-decoration: none;
  font-size: 18px;
  font-weight: 500;
  transition: color 0.3s ease;
  position: relative;
}

.nav-link:hover {
  color: #000;
}

.nav-link.router-link-active {
  color: #000;
}

.nav-link.router-link-active::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  right: 0;
  height: 2px;
  background: #000;
  border-radius: 2px;
}

/* Правая часть - поиск и действия */
.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-shrink: 0;
}

.search-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  background: #f5f5f5;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  color: #333;
  transition: all 0.3s ease;
}

.search-btn:hover {
  background: #e5e5e5;
  color: #000;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.action-btn {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  background: #f5f5f5;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  color: #333;
  transition: all 0.3s ease;
}

.action-btn:hover {
  background: #e5e5e5;
  color: #000;
}

.cart-btn {
  padding-right: 24px;
}

.cart-count {
  position: absolute;
  top: 8px;
  right: 8px;
  min-width: 20px;
  height: 20px;
  padding: 0 6px;
  background: #000;
  color: white;
  font-size: 12px;
  font-weight: 600;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Адаптивность */
@media (max-width: 1024px) {
  .header .container {
    gap: 24px;
  }

  .header-center {
    gap: 32px;
  }
}

@media (max-width: 768px) {
  .header-container {
    width: 100%;
  }

  .container {
    padding: 0 16px;
  }

  .header .container {
    flex-direction: column;
    align-items: stretch;
    gap: 20px;
  }

  .header-left,
  .header-center,
  .header-right {
    width: 100%;
  }

  .header-left {
    display: flex;
    justify-content: center;
  }

  .header-center {
    justify-content: center;
    gap: 40px;
  }

  .header-right {
    flex-direction: column;
    align-items: center;
  }

  .header-actions {
    width: 100%;
    justify-content: center;
  }

  .search-btn,
  .action-btn {
    width: 48px;
    height: 48px;
  }
}
</style>
