<template>
  <div class="hero h-full bg-base-200">
    <div class="hero-content text-center">
      <div class="max-w-md">
        <h1 class="text-5xl font-bold">{{ props.title }}</h1>
        <p class="py-6">{{ props.description }}</p>
        <slot name="content">
          <router-link :to="{ name: 'HomeView' }" class="btn btn-primary"
            ><i class="fas fa-home" /> Go to Homepage</router-link
          >
        </slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  title: {
    type: String,
    required: false,
    default: "That's an error!"
  },
  description: {
    type: String,
    required: false,
    default: "Sorry but something went wrong!"
  }
});
</script>
