<template>
  <div v-if="role">
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, inject } from "vue";
import type { Ref } from "vue";
import type { Role } from "@/types/resources/role";
import type { Response } from "@/types/response";
import { useRoleStore } from "@/stores/role";

const store = useRoleStore();

const props = defineProps({
  id: {
    type: String,
    required: true
  }
});

const role: Ref<Role | null> = ref(null)

const setToolBarSubtitle = inject("setToolBarSubtitle") as Function;

onMounted(() => {
  store.readRole(Number(props.id)).then((response: Response<Role>) => {
    role.value = response.data
    setToolBarSubtitle(response.data.name)
  })
});
</script>
