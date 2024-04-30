<template>
  <router-view />
</template>

<script setup lang="ts">
import { inject, onMounted } from "vue";
import { useIdentityStore } from "@/stores/auth/identity";

const store = useIdentityStore();

const setToolBarTitle = inject("setToolBarTitle") as Function;
const setToolBarSubtitle = inject("setToolBarSubtitle") as Function;

onMounted(() => {
  store.readIdentity();
  setToolBarTitle("Profile");
  setToolBarSubtitle("");
});
</script>
