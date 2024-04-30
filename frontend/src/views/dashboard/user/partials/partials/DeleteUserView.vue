<template>
  <div class="flex flex-col gap-2 w-full">
    <user-grid
      v-if="store.user"
      :records="[store.user]"
      :exclude-columns="['actions']"
    />
    <p>Are you sure you want to delete this user?</p>
    <button class="btn btn-error" @click="deleteClicked">Delete</button>
  </div>
</template>
<script setup lang="ts">
import { onMounted, inject } from "vue";
import { useUserStore } from "@/stores/user";
import type { User } from '@/types/resources/user'
import type { Response } from '@/types/response'
import { useToast } from 'vue-toastification'
import { useRouter } from 'vue-router'
import UserGrid from "@/components/display/dataGrids/user/UserGrid.vue";

const store = useUserStore();
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
  store.deleteUser(Number(props.id)).then((response: Response) => {
    toast.success(response.message)
    router.push({name: 'UsersIndexView'})
  })
}

onMounted(() => {
  setToolBarItems([
    { name: "Back", method: router.back, icon: "fa fa-arrow-left" }
  ]);
});
</script>
