<template>
  <div v-if="store.identity" class="flex flex-col gap-6">
    <data-display class="w-full" :display-items="displayItems" />
    <h2 class="text-2xl font-bold">Currently held roles</h2>
    <role-grid
      :records="store.identity.roles!"
      :exclude-columns="['actions']"
    />
  </div>
</template>
<script setup lang="ts">
import { onMounted, inject, computed } from "vue";
import { useIdentityStore } from "@/stores/auth/identity";
import DataDisplay from "@/components/display/DataDisplay.vue";
import RoleGrid from "@/components/display/dataGrids/role/RoleGrid.vue";

const store = useIdentityStore();

const displayItems = computed(() => [
  {
    title: "User ID",
    value: store.identity?.id
  },
  {
    title: "Username",
    value: store.identity?.username
  },
  {
    title: "User status",
    value: store.identity?.is_disabled ? "Disabled" : "Active"
  },
  {
    title: "User has",
    value: store.identity?.roles!.length,
    description: "Roles"
  }
]);

const setToolBarItems = inject("setToolBarItems") as Function;

onMounted(() => {
  setToolBarItems([
    {
      name: "Update",
      url: { name: "UpdateProfileView" },
      icon: "fa fa-pen-to-square"
    },
    {
      name: "Delete",
      url: { name: "DeleteProfileView" },
      icon: "fa fa-trash-can"
    }
  ]);
});
</script>
