<template>
  <div class="shop-view">
    <Header @search="handleSearch" />
    <BottomPanel @search="handleSearch" />

    <main class="main">
      <div class="container">
        <h1>Магазин</h1>
        
        <div class="content">
          <aside class="sidebar">
            <CategoryFilter
              :categories="categories"
              :selected-category="selectedCategory"
              @select-category="handleCategorySelect"
            />
          </aside>

          <section class="products-section">
            <div v-if="searchQuery" class="search-results">
              <h2>Результаты поиска: "{{ searchQuery }}"</h2>
              <button @click="clearSearch" class="clear-search-btn">Очистить</button>
            </div>

            <ProductList
              :products="products"
              :loading="loading"
              :error="error"
              @retry="loadProducts"
            />
          </section>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useProductsStore } from '@/stores/products'
import Header from '@/components/Header.vue'
import BottomPanel from '@/components/BottomPanel.vue'
import CategoryFilter from '@/components/CategoryFilter.vue'
import ProductList from '@/components/ProductList.vue'

const productsStore = useProductsStore()

const searchQuery = ref('')
const selectedCategory = ref<string | null>(null)

const products = computed(() => productsStore.products)
const loading = computed(() => productsStore.loading)
const error = computed(() => productsStore.error)
const categories = computed(() => productsStore.categories)

async function loadProducts() {
  const params: any = { skip: 0, limit: 100 }
  if (selectedCategory.value) {
    params.category = selectedCategory.value
  }
  await productsStore.fetchProducts(params)
}

function handleSearch(query: string) {
  searchQuery.value = query
  if (query.trim()) {
    productsStore.searchProducts(query)
  }
}

function clearSearch() {
  searchQuery.value = ''
  loadProducts()
}

function handleCategorySelect(category: string | null) {
  selectedCategory.value = category
  loadProducts()
}

onMounted(() => {
  loadProducts()
})
</script>

<style scoped>
.shop-view {
  min-height: 100vh;
  background: #f8f9fa;
}

.main {
  padding: 32px 0;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 20px;
}

h1 {
  font-size: 32px;
  font-weight: 700;
  color: #000;
  margin-bottom: 32px;
}

.content {
  display: flex;
  gap: 32px;
  align-items: flex-start;
}

.sidebar {
  width: 250px;
  flex-shrink: 0;
  position: sticky;
  top: 32px;
}

.products-section {
  flex: 1;
}

.search-results {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding: 16px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.search-results h2 {
  font-size: 18px;
  font-weight: 600;
  color: #000;
  margin: 0;
}

.clear-search-btn {
  padding: 8px 16px;
  background: #000;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.3s ease;
}

.clear-search-btn:hover {
  background: #000;
}

@media (max-width: 768px) {
  .content {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    position: static;
  }
}
</style>
