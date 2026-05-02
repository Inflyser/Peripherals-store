<template>
  <div class="product-card" @click="goToProduct">
    <div class="product-image">
      <img v-if="product.image_url" :src="product.image_url" :alt="product.name" />
      <div v-else class="placeholder-image">
        <span>{{ product.name.charAt(0) }}</span>
      </div>
    </div>
    <div class="product-info">
      <h3 class="product-name">{{ product.name }}</h3>
      <p class="product-category">{{ product.category }}</p>
      <p class="product-description">{{ truncatedDescription }}</p>
      <div class="product-footer">
        <span class="product-price">{{ formatPrice(product.price) }} ₽</span>
        <span class="product-stock" :class="{ 'low-stock': product.stock < 5 }">
          {{ product.stock > 0 ? `В наличии: ${product.stock}` : 'Нет в наличии' }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import type { Product } from '@/types/product'

const props = defineProps<{
  product: Product
}>()

const router = useRouter()

const truncatedDescription = computed(() => {
  if (!props.product.description) return ''
  return props.product.description.length > 80
    ? props.product.description.substring(0, 80) + '...'
    : props.product.description
})

function formatPrice(price: number): string {
  return price.toLocaleString('ru-RU')
}

function goToProduct() {
  router.push({ name: 'product', params: { id: props.product.id } })
}
</script>

<style scoped>
.product-card {
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
  background: white;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.product-image {
  width: 100%;
  height: 200px;
  background: #eee;
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
  background: linear-gradient(135deg, #000 0%, #000 100%);
  color: white;
  font-size: 48px;
  font-weight: bold;
}

.product-info {
  padding: 16px;
}

.product-name {
  margin: 0 0 8px 0;
  font-size: 18px;
  font-weight: 600;
  color: #000;
}

.product-category {
  margin: 0 0 8px 0;
  font-size: 14px;
  color: #444;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.product-description {
  margin: 0 0 12px 0;
  font-size: 14px;
  color: #444;
  line-height: 1.4;
}

.product-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.product-price {
  font-size: 20px;
  font-weight: 700;
  color: #000;
}

.product-stock {
  font-size: 12px;
  color: #4caf50;
}

.product-stock.low-stock {
  color: #ff9800;
}

.product-stock:empty::before {
  content: 'Нет в наличии';
  color: #f44336;
}
</style>
