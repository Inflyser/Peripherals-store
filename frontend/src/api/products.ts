import apiClient from './client'
import type { Product, ProductCreate, ProductUpdate } from '@/types/product'

export const productsApi = {
  async getAll(params?: { skip?: number; limit?: number; category?: string }) {
    const response = await apiClient.get<Product[]>('/products/', { params })
    return response.data
  },

  async search(query: string, params?: { skip?: number; limit?: number }) {
    const response = await apiClient.get<Product[]>('/products/search/', {
      params: { q: query, ...params }
    })
    return response.data
  },

  async getById(id: number) {
    const response = await apiClient.get<Product>(`/products/${id}/`)
    return response.data
  },

  async create(product: ProductCreate) {
    const response = await apiClient.post<Product>('/products/', product)
    return response.data
  },

  async update(id: number, product: ProductUpdate) {
    const response = await apiClient.put<Product>(`/products/${id}/`, product)
    return response.data
  },

  async delete(id: number) {
    await apiClient.delete(`/products/${id}/`)
  }
}
