<template>
  <form class="card-body" @submit.prevent="submitClicked">
    <text-input
      v-model="state.username"
      label="Username"
      placeholder="username"
      :is-required="true"
    />
    <div class="collapse collapse-arrow bg-base-200 mt-2">
      <input type="checkbox" />
      <div class="collapse-title text-xl font-medium">
        <button class="btn btn-neutral">Change Password</button>
      </div>
      <div class="collapse-content">
        <text-input
          v-model="state.newPassword"
          label="Password"
          type="password"
          placeholder="password"
        />
        <text-input
          v-model="state.confirmNewPassword"
          label="Confirm Password"
          type="password"
          placeholder="confirm password"
        />
      </div>
    </div>
    <text-input
      v-model="state.password"
      label="Current Password"
      type="password"
      placeholder="current password"
      :is-required="true"
    />
    <div class="form-control mt-6">
      <button class="btn btn-primary">Submit</button>
    </div>
  </form>
</template>
<script setup lang="ts">
import { reactive, onMounted, inject } from "vue";
import { useIdentityStore } from "@/stores/auth/identity";
import type { UpdateIdentityPayload } from '@/types/payloads/auth/identity'
import TextInput from "@/components/input/TextInput.vue";
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

const store = useIdentityStore();
const router = useRouter()
const toast = useToast()

const state = reactive({
  username: store.identity?.username,
  newPassword: "",
  confirmNewPassword: "",
  password: ""
});

const createPayload = (): UpdateIdentityPayload | undefined => {
  let payload = {} as UpdateIdentityPayload
  if (!state.username) {
    toast.warning('Username cannot be empty')
    return
  }
  if (!state.password) {
    toast.warning('Please enter your current password')
    return
  }
  if (state.newPassword !== state.confirmNewPassword) {
    toast.warning('New passwords must match')
    return
  }

  if (state.username !== store.identity!.username) {
    payload.username = state.username
  }
  if (state.newPassword) {
    payload.new_password = state.newPassword
  }
  payload.password = state.password
  return payload
}

const submitClicked = () => {
  const payload = createPayload()
  if (payload) {
    store.updateIdentity(payload).then(response => {
      toast.success(response.message);
      router.push({ name: "ProfileIndexView" });
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
