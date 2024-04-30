<template>
  <div class="flex flex-col gap-2 w-full">
    <user-grid
      v-if="identityStore.identity"
      :records="[identityStore.identity]"
      :exclude-columns="['actions']"
    />
    <p>
      Please confirm you want to delete your account by entering your current
      password
    </p>
    <form class="card-body" @submit.prevent="submitClicked">
      <text-input
        v-model="state.password"
        label="Current Password"
        placeholder="current password"
        type="password"
        :is-required="true"
      />
      <div class="form-control mt-6">
        <button class="btn btn-primary">Submit</button>
      </div>
    </form>
  </div>
</template>
<script setup lang="ts">
import { reactive, inject, onMounted } from "vue";
import TextInput from "@/components/input/TextInput.vue";
import { useRouter } from "vue-router";
import { useIdentityStore } from "@/stores/auth/identity";
import { useAuthStore } from "@/stores/auth";
import { useToast } from "vue-toastification";
import type { DeleteIdentityPayload } from '@/types/payloads/auth/identity'
import UserGrid from "@/components/display/dataGrids/user/UserGrid.vue";

const identityStore = useIdentityStore();
const authStore = useAuthStore();
const router = useRouter();
const toast = useToast();

const state = reactive({
  password: ""
});

const createPayload = (): DeleteIdentityPayload | undefined => {
  if (!state.password) {
    toast.warning('Please enter your current password')
    return
  }
  return { password: state.password }
}

const submitClicked = () => {
  const payload = createPayload()
  if (payload) {
  identityStore.deleteIdentity(payload).then(response => {
    toast.success(response.message);
    authStore.logout();
    router.push({ name: "HomeView" });
  });
}
};

const setToolBarItems = inject("setToolBarItems") as Function;

onMounted(() => {
  setToolBarItems([
    { name: "Back", method: router.back, icon: "fa fa-arrow-left" }
  ]);
});
</script>
