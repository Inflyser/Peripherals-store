<template>
  <div class="category-filter">
    <h3 class="filter-title">Категории</h3>
    <div class="category-list">
      <button
        v-for="category in categories"
        :key="category"
        @click="selectCategory(category)"
        :class="['category-button', { active: selectedCategory === category }]"
      >
        {{ category }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  categories: string[]
  selectedCategory: string | null
}>()

const emit = defineEmits<{
  'select-category': [category: string | null]
}>()

function selectCategory(category: string) {
  emit('select-category', category)
}
</script>

<style scoped>
.category-filter {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.filter-title {
  margin: 0 0 16px 0;
  font-size: 18px;
  font-weight: 600;
  color: #000;
}

.category-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.category-button {
  padding: 10px 16px;
  background: transparent;
  color: #444;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  text-align: left;
  font-size: 14px;
  transition: all 0.3s ease;
}

.category-button:hover {
  background: #eee;
  border-color: #000;
}

.category-button.active {
  background: #000;
  color: white;
  border-color: #000;
}
</style>
