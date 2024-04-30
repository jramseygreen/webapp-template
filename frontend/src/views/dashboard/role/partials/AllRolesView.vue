<template>
  <role-grid :records="store.roles" />
</template>
<script setup lang="ts">
import { onMounted, inject } from "vue";
import { useRoleStore } from "@/stores/role";
import RoleGrid from "@/components/display/dataGrids/role/RoleGrid.vue";

const store = useRoleStore();

const setToolBarItems = inject("setToolBarItems") as Function;
const setToolBarSubtitle = inject("setToolBarSubtitle") as Function;

onMounted(() => {
  store.allRoles();
  setToolBarItems([
    { name: "Create", url: { name: "CreateRoleView" }, icon: "fa fa-plus" }
  ]);
  setToolBarSubtitle("");
});
</script>
