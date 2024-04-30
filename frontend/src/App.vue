<template>
  <nav-bar />
  <div class="h-[calc(100vh-72px)]">
    <router-view />
  </div>
</template>

<script setup lang="ts">
import NavBar from "@/components/display/navigation/NavBar.vue";
</script>
