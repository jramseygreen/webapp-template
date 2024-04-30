<template>
  <div v-if="store.role" class="flex flex-col gap-6">
    <data-display class="w-full" :displayItems="displayItems" />
    <h2 class="text-2xl font-bold">Current Users With Role</h2>
    <user-grid :records="store.role.users" :exclude-columns="['roles']" />
  </div>
</template>
<script setup lang="ts">
import { onMounted, inject, computed } from "vue";
import { useRoleStore } from "@/stores/role";
import type { Role } from '@/types/resources/role'
import UserGrid from "@/components/display/dataGrids/user/UserGrid.vue";
import DataDisplay from "@/components/display/DataDisplay.vue";
import { useRouter } from 'vue-router'

const router = useRouter();
const store = useRoleStore();

const displayItems = computed(() =>
   [
    {
      title: 'ID',
      value: store.role?.id
    },
    {
      title: 'Name',
      value: store.role?.name
    },
    {
      title: 'In use by',
      value: store.role?.users!.length,
      description: 'Users'
    }
  ]
)

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
      url: { name: "UpdateRoleView", params: { id: props.id } },
      icon: "fa fa-pen-to-square",
      isDisabled: store.role?.name === 'admin'
    },
    {
      name: "Delete",
      url: { name: "DeleteRoleView", params: { id: props.id } },
      icon: "fa fa-trash-can",
      isDisabled: store.role?.name === 'admin'
    }
  ]);
});
</script>
