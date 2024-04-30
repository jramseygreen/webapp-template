<template>
  <user-grid :records="store.users" />
</template>
<script setup lang="ts">
import { onMounted, inject } from "vue";
import { useUserStore } from "@/stores/user";
import UserGrid from "@/components/display/dataGrids/user/UserGrid.vue";

const store = useUserStore();

const setToolBarItems = inject("setToolBarItems") as Function;
const setToolBarSubtitle = inject("setToolBarSubtitle") as Function;

onMounted(() => {
  store.allUsers();
  setToolBarItems([
    { name: "Create", url: { name: "CreateUserView" }, icon: "fa fa-plus" }
  ]);
  setToolBarSubtitle("");
});
</script>
