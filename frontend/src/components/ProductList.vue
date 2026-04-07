<template>
  <div class="product-list">
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>Загрузка товаров...</p>
    </div>

    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
      <button @click="retry" class="retry-button">Попробовать снова</button>
    </div>

    <div v-else-if="products.length === 0" class="empty">
      <p>Товары не найдены</p>
    </div>

    <div v-else class="products-grid">
      <ProductCard
        v-for="product in products"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import ProductCard from './ProductCard.vue'

const props = defineProps<{
  products: any[]
  loading: boolean
  error: string | null
}>()

const emit = defineEmits<{
  retry: []
}>()

function retry() {
  emit('retry')
}
</script>

<style scoped>
.product-list {
  width: 100%;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: #666;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error {
  text-align: center;
  padding: 60px 20px;
  color: #f44336;
}

.retry-button {
  margin-top: 16px;
  padding: 10px 24px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.3s ease;
}

.retry-button:hover {
  background: #5568d3;
}

.empty {
  text-align: center;
  padding: 60px 20px;
  color: #999;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
  padding: 20px 0;
}

@media (max-width: 768px) {
  .products-grid {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px;
  }
}
</style>
