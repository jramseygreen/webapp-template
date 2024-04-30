<template>
  <div class="stats shadow border">
    <div
      v-for="(displayItem, index) in props.displayItems"
      :key="index"
      class="stat"
    >
      <div class="stat-title">{{ displayItem.title }}</div>
      <div class="stat-value">{{ displayItem.value }}</div>
      <div v-if="displayItem.description" class="stat-desc">
        {{ displayItem.description }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { PropType } from 'vue'
import type { DisplayItem } from '@/types/components/display/dataDisplay'

const props = defineProps({
  displayItems: {
    type: Array as PropType<DisplayItem[]>,
    required: false,
    default: () => []
  }
});
</script>
