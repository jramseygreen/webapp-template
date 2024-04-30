<template>
  <router-view />
</template>

<script setup lang="ts">
import { inject, onMounted } from "vue";

const setToolBarTitle = inject("setToolBarTitle") as Function;
const setToolBarSubtitle = inject("setToolBarSubtitle") as Function;

onMounted(() => {
  setToolBarTitle("Roles");
  setToolBarSubtitle("");
});
</script>
