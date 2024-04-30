<template>
  <error-template :title="props.title" :description="props.description" />
</template>

<script setup lang="ts">
import ErrorTemplate from "@/components/display/errors/ErrorTemplate.vue";

const props = defineProps({
  title: {
    type: String,
    required: false
  },
  description: {
    type: String,
    required: false
  }
});
</script>
