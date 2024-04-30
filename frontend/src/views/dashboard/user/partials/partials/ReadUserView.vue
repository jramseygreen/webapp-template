<template>
  <div v-if="store.user" class="flex flex-col gap-6">
    <data-display class="w-full" :display-items="displayItems" />
    <h2 class="text-2xl font-bold">Currently held roles</h2>
    <role-grid :records="store.user.roles!" />
  </div>
</template>
<script setup lang="ts">
import { onMounted, inject, computed } from "vue";
import { useUserStore } from "@/stores/user";
import DataDisplay from "@/components/display/DataDisplay.vue";
import RoleGrid from "@/components/display/dataGrids/role/RoleGrid.vue";
import { useRouter } from "vue-router";

const router = useRouter();
const store = useUserStore();

const displayItems = computed(() => [
  {
    title: "User ID",
    value: store.user?.id
  },
  {
    title: "Username",
    value: store.user?.username
  },
  {
    title: "User status",
    value: store.user?.is_disabled ? "Disabled" : "Active"
  },
  {
    title: "User has",
    value: store.user?.roles!.length,
    description: "Roles"
  }
]);

const props = defineProps({
  id: {
    type: String,
    required: true
  }
});

const setToolBarItems = inject("setToolBarItems") as Function;

onMounted(() => {
  setToolBarItems([
    { name: "Back", method: router.back, icon: "fa fa-arrow-left" },
    {
      name: "Update",
      url: { name: "UpdateUserView", params: { id: props.id } },
      icon: "fa fa-pen-to-square"
    },
    {
      name: "Delete",
      url: { name: "DeleteUserView", params: { id: props.id } },
      icon: "fa fa-trash-can"
    }
  ]);
});
</script>
