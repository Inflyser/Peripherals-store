import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/shop',
      name: 'shop',
      component: () => import('@/views/ShopView.vue')
    },
    {
      path: '/blog',
      name: 'blog',
      component: () => import('@/views/BlogView.vue')
    },
    {
      path: '/product/:id',
      name: 'product',
      component: () => import('@/views/ProductView.vue')
    },
    {
      path: '/category/:category',
      name: 'category',
      component: HomeView
    }
  ]
})

export default router
