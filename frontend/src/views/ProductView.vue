<template>
  <div class="product-view">
    <Header @search="handleSearch" />
    <BottomPanel @search="handleSearch" />
    <div class="container">
      <button @click="goBack" class="back-button">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="19" y1="12" x2="5" y2="12"></line>
          <polyline points="12 19 5 12 12 5"></polyline>
        </svg>
        Назад
      </button>

      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Загрузка товара...</p>
      </div>

      <div v-else-if="error" class="error">
        <p>{{ error }}</p>
        <button @click="loadProduct" class="retry-button">Попробовать снова</button>
      </div>

      <div v-else-if="product" class="product-detail">
        <div class="product-gallery">
          <div class="product-image">
            <img v-if="product.image_url" :src="product.image_url" :alt="product.name" />
            <div v-else class="placeholder-image">
              <span>{{ product.name.charAt(0) }}</span>
            </div>
          </div>
        </div>

        <div class="product-info">
          <span class="product-category">{{ product.category }}</span>
          <h1 class="product-name">{{ product.name }}</h1>

          <div class="product-price">
            <span class="price">{{ formatPrice(product.price) }} ₽</span>
            <span class="stock" :class="{ 'low-stock': product.stock < 5, 'out-of-stock': product.stock === 0 }">
              {{ product.stock > 0 ? `В наличии: ${product.stock} шт.` : 'Нет в наличии' }}
            </span>
          </div>

          <div v-if="product.description" class="product-description">
            <h3>Описание</h3>
            <p>{{ product.description }}</p>
          </div>

          <div class="product-actions">
            <button
              class="add-to-cart-button"
              :disabled="product.stock === 0"
              @click="addToCart"
            >
              {{ product.stock > 0 ? 'Добавить в корзину' : 'Нет в наличии' }}
            </button>
          </div>
        </div>
      </div>

      <div v-else class="not-found">
        <p>Товар не найден</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useProductsStore } from '@/stores/products'
import type { Product } from '@/types/product'
import Header from '@/components/Header.vue'
import BottomPanel from '@/components/BottomPanel.vue'

const route = useRoute()
const router = useRouter()
const productsStore = useProductsStore()

const loading = ref(false)
const error = ref<string | null>(null)

const product = computed<Product | undefined>(() => {
  const id = Number(route.params.id)
  return productsStore.getProductById(id)
})

async function loadProduct() {
  const id = Number(route.params.id)
  loading.value = true
  error.value = null
  try {
    await productsStore.fetchProductById(id)
  } catch (e: any) {
    error.value = e.message || 'Ошибка загрузки товара'
  } finally {
    loading.value = false
  }
}

function goBack() {
  router.back()
}

function formatPrice(price: number): string {
  return price.toLocaleString('ru-RU')
}

function addToCart() {
  alert('Функция корзины будет добавлена позже')
}

function handleSearch(query: string) {
  // Перейти на главную страницу с поисковым запросом
  router.push({ name: 'home', query: { search: query } })
}

onMounted(() => {
  if (!product.value) {
    loadProduct()
  }
})
</script>

<style scoped>
.product-view {
  min-height: 100vh;
  background: #f8f9fa;
  padding-top: 32px;
}

.back-button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: white;
  color: #666;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  margin-bottom: 24px;
  transition: all 0.3s ease;
}

.back-button:hover {
  background: #f5f5f5;
  border-color: #667eea;
  color: #667eea;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 100px 20px;
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
  padding: 100px 20px;
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

.not-found {
  text-align: center;
  padding: 100px 20px;
  color: #999;
}

.product-detail {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  background: white;
  border-radius: 16px;
  padding: 32px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.product-gallery {
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-image {
  width: 100%;
  aspect-ratio: 1;
  background: #f5f5f5;
  border-radius: 12px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.placeholder-image {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  font-size: 96px;
  font-weight: bold;
}

.product-info {
  display: flex;
  flex-direction: column;
}

.product-category {
  display: inline-block;
  padding: 6px 12px;
  background: #f0f0f0;
  color: #666;
  border-radius: 6px;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 16px;
  align-self: flex-start;
}

.product-name {
  margin: 0 0 24px 0;
  font-size: 32px;
  font-weight: 700;
  color: #333;
  line-height: 1.2;
}

.product-price {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 32px;
}

.price {
  font-size: 36px;
  font-weight: 700;
  color: #667eea;
}

.stock {
  padding: 6px 12px;
  background: #e8f5e9;
  color: #4caf50;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
}

.stock.low-stock {
  background: #fff3e0;
  color: #ff9800;
}

.stock.out-of-stock {
  background: #ffebee;
  color: #f44336;
}

.product-description {
  margin-bottom: 32px;
}

.product-description h3 {
  margin: 0 0 12px 0;
  font-size: 18px;
  font-weight: 600;
  color: #333;
}

.product-description p {
  margin: 0;
  color: #666;
  line-height: 1.6;
}

.product-actions {
  margin-top: auto;
}

.add-to-cart-button {
  width: 100%;
  padding: 16px 32px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.add-to-cart-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
}

.add-to-cart-button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .product-detail {
    grid-template-columns: 1fr;
    gap: 24px;
    padding: 20px;
  }

  .product-name {
    font-size: 24px;
  }

  .price {
    font-size: 28px;
  }
}
</style>
