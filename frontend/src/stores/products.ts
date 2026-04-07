import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { productsApi } from '@/api/products'
import type { Product, ProductCreate, ProductUpdate } from '@/types/product'

export const useProductsStore = defineStore('products', () => {
  const products = ref<Product[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  const categories = computed(() => {
    const uniqueCategories = new Set(products.value.map(p => p.category))
    return Array.from(uniqueCategories)
  })

  async function fetchProducts(params?: { skip?: number; limit?: number; category?: string }) {
    loading.value = true
    error.value = null
    try {
      products.value = await productsApi.getAll(params)
    } catch (e: any) {
      error.value = e.message || 'Ошибка загрузки товаров'
      console.error('Error fetching products:', e)
    } finally {
      loading.value = false
    }
  }

  async function searchProducts(query: string) {
    loading.value = true
    error.value = null
    try {
      products.value = await productsApi.search(query)
    } catch (e: any) {
      error.value = e.message || 'Ошибка поиска товаров'
      console.error('Error searching products:', e)
    } finally {
      loading.value = false
    }
  }

  async function fetchProductById(id: number) {
    loading.value = true
    error.value = null
    try {
      const product = await productsApi.getById(id)
      const index = products.value.findIndex(p => p.id === id)
      if (index !== -1) {
        products.value[index] = product
      }
      return product
    } catch (e: any) {
      error.value = e.message || 'Ошибка загрузки товара'
      console.error('Error fetching product:', e)
      throw e
    } finally {
      loading.value = false
    }
  }

  async function createProduct(product: ProductCreate) {
    loading.value = true
    error.value = null
    try {
      const newProduct = await productsApi.create(product)
      products.value.push(newProduct)
      return newProduct
    } catch (e: any) {
      error.value = e.message || 'Ошибка создания товара'
      console.error('Error creating product:', e)
      throw e
    } finally {
      loading.value = false
    }
  }

  async function updateProduct(id: number, product: ProductUpdate) {
    loading.value = true
    error.value = null
    try {
      const updatedProduct = await productsApi.update(id, product)
      const index = products.value.findIndex(p => p.id === id)
      if (index !== -1) {
        products.value[index] = updatedProduct
      }
      return updatedProduct
    } catch (e: any) {
      error.value = e.message || 'Ошибка обновления товара'
      console.error('Error updating product:', e)
      throw e
    } finally {
      loading.value = false
    }
  }

  async function deleteProduct(id: number) {
    loading.value = true
    error.value = null
    try {
      await productsApi.delete(id)
      products.value = products.value.filter(p => p.id !== id)
    } catch (e: any) {
      error.value = e.message || 'Ошибка удаления товара'
      console.error('Error deleting product:', e)
      throw e
    } finally {
      loading.value = false
    }
  }

  function getProductById(id: number) {
    return products.value.find(p => p.id === id)
  }

  return {
    products,
    loading,
    error,
    categories,
    fetchProducts,
    searchProducts,
    fetchProductById,
    createProduct,
    updateProduct,
    deleteProduct,
    getProductById
  }
})
