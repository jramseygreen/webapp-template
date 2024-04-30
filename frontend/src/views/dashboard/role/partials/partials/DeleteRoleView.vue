<template>
  <div class="flex flex-col gap-2 w-full">
    <role-grid
      v-if="store.role"
      :records="[store.role]"
      :exclude-columns="['actions']"
    />
    <p>Are you sure you want to delete this role?</p>
    <button class="btn btn-error" @click="deleteClicked">Delete</button>
  </div>
</template>
<script setup lang="ts">
import { onMounted, inject } from "vue";
import { useRoleStore } from "@/stores/role";
import type { Role } from '@/types/resources/role'
import type { Response } from '@/types/response'
import { useToast } from 'vue-toastification'
import { useRouter } from 'vue-router'
import RoleGrid from "@/components/display/dataGrids/role/RoleGrid.vue";

const store = useRoleStore();
const router = useRouter();
const toast = useToast()

const props = defineProps({
  id: {
    type: String,
    required: true
  }
});

const setToolBarItems = inject("setToolBarItems") as Function;

const deleteClicked = () => {
  store.deleteRole(Number(props.id)).then((response: Response) => {
    toast.success(response.message)
    router.push({name: 'RolesIndexView'})
  })
}

onMounted(() => {
  setToolBarItems([
    { name: "Back", method: router.back, icon: "fa fa-arrow-left" }
  ]);
});
</script>
