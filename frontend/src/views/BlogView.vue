<template>
  <div class="blog-view">
    <Header @search="handleSearch" />
    <BottomPanel @search="handleSearch" />
    <main class="main">
      <div class="container">
        <h1>Блог</h1>
        <p>Страница блога в разработке</p>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import Header from '@/components/Header.vue'
import BottomPanel from '@/components/BottomPanel.vue'

const router = useRouter()

function handleSearch(query: string) {
  router.push({ name: 'home', query: { search: query } })
}
</script>

<style scoped>
.blog-view {
  min-height: 200vh;
  background: #f8f9fa;
}

.main {
  padding: 32px 0;
}

h1 {
  font-size: 32px;
  font-weight: 700;
  color: #333;
  margin-bottom: 16px;
}

p {
  font-size: 16px;
  color: #666;
}
</style>
