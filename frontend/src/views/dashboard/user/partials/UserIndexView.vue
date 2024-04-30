<template>
  <div v-if="user">
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, inject } from "vue";
import type { Ref } from "vue";
import type { User } from "@/types/resources/user";
import type { Response } from "@/types/response";
import { useUserStore } from "@/stores/user";

const store = useUserStore();

const props = defineProps({
  id: {
    type: String,
    required: true
  }
});

const user: Ref<User | null> = ref(null)

const setToolBarSubtitle = inject("setToolBarSubtitle") as Function;

onMounted(() => {
  store.readUser(Number(props.id)).then((response: Response<User>) => {
    user.value = response.data
    setToolBarSubtitle(response.data.username)
  })
});
</script>
