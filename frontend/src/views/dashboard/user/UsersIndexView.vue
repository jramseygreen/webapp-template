<template>
  <router-view />
</template>

<script setup lang="ts">
import { onMounted, inject } from "vue";

const setToolBarTitle = inject("setToolBarTitle") as Function;
const setToolBarSubtitle = inject("setToolBarSubtitle") as Function;

onMounted(() => {
  setToolBarTitle("Users");
  setToolBarSubtitle("");
});
</script>
