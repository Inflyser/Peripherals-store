<template>
  <div class="home-view">
    <Header @search="handleSearch" />
    <BottomPanel @search="handleSearch" />

    <main class="main">
      <div class="container">
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
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useProductsStore } from '@/stores/products'
import Header from '@/components/Header.vue'
import BottomPanel from '@/components/BottomPanel.vue'
import CategoryFilter from '@/components/CategoryFilter.vue'
import ProductList from '@/components/ProductList.vue'

const route = useRoute()
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

watch(() => route.params.category, (newCategory) => {
  if (typeof newCategory === 'string') {
    selectedCategory.value = newCategory
    loadProducts()
  }
})
</script>

<style scoped>
.home-view {
  min-height: 100vh;
  background: #f8f9fa;
}

.main {
  padding: 48px 0 48px 0;
  background: #eee;
  min-height: calc(100vh - 200px);
}

.content {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 32px;
}

.sidebar {
  position: sticky;
  top: 100px;
  height: fit-content;
}

.products-section {
  min-height: 400px;
}

.search-results {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  padding: 16px 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.search-results h2 {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
  color: #000;
}

.clear-search-btn {
  padding: 8px 16px;
  background: #eee;
  color: #444;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s ease;
}

.clear-search-btn:hover {
  background: #e0e0e0;
}

@media (max-width: 1024px) {
  .content {
    grid-template-columns: 1fr;
  }

  .sidebar {
    position: static;
  }
}

</style>
