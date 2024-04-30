<template>
  <div class="hero h-full bg-base-200">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="text-center lg:text-left">
        <h1 class="text-5xl font-bold">Register</h1>
        <p class="py-6">This should be a tagline for your app.</p>
      </div>
      <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
        <form class="card-body" @submit.prevent="registerClicked">
          <text-input
            v-model="state.username"
            label="Username"
            placeholder="username"
            :is-required="true"
          />
          <text-input
            v-model="state.password"
            label="Password"
            type="password"
            placeholder="password"
            :is-required="true"
          />
          <text-input
            v-model="state.confirmPassword"
            label="Confirm Password"
            type="password"
            placeholder="confirm password"
            :is-required="true"
          />
          <label class="label">
            <router-link
              :to="{ name: 'LoginView' }"
              class="label-text-alt link link-hover"
              >Login</router-link
            >
          </label>
          <div class="form-control mt-6">
            <button class="btn btn-primary">Register</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import type { CreateIdentityPayload } from '@/types/payloads/auth/identity'
import { useAuthStore } from '@/stores/auth'
import { useIdentityStore } from '@/stores/auth/identity'
import { useSettingStore } from '@/stores/setting'
import TextInput from '@/components/input/TextInput.vue'

const authStore = useAuthStore()
const identityStore = useIdentityStore()
const settingStore = useSettingStore()
const toast = useToast();
const router = useRouter();

const state = reactive({
  username: "",
  password: "",
  confirmPassword: ""
});

const createPayload = (): CreateIdentityPayload | undefined => {
  if (!state.username) {
    toast.warning('You must enter a username')
    return
  }
  if (!state.password) {
    toast.warning('You must enter a password')
    return
  }
  if (state.password !== state.confirmPassword) {
    toast.warning('Passwords must match!')
    return
  }

  return {username: state.username, password: state.password}
}

const registerClicked = () => {
  const payload = createPayload()
  if (payload) {
    identityStore.createIdentity(payload).then(response => {
      toast.success(response.message);
      router.push({ name: "LoginView" });
    });
  }
};

onMounted(() => {
  if (authStore.isAuthed || !settingStore.isRegistrationEnabled) {
    if (!settingStore.isRegistrationEnabled) {
      toast.warning('Registration is currently disabled!')
    }
    router.replace({ name: "HomeView" });
  }
});
</script>
