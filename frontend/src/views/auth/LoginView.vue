<template>
  <div class="hero h-full bg-base-200">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="text-center lg:text-left">
        <h1 class="text-5xl font-bold">Login now!</h1>
        <p class="py-6">This should be a tagline for your app.</p>
      </div>
      <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
        <form class="card-body" @submit.prevent="loginClicked">
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
          <div class="form-control">
            <div class="flex justify-between">
              <router-link
                :to="{ name: 'RegisterView' }"
                class="label-text-alt link link-hover"
                >Register</router-link
              >
              <div class="flex align-items-center gap-2">
                <span class="label-text">Remember Me</span>
                <input
                  v-model="state.rememberMe"
                  type="checkbox"
                  class="checkbox"
                />
              </div>
            </div>
          </div>
          <div class="form-control mt-6">
            <button class="btn btn-primary">
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useToast } from "vue-toastification";
import { useAuthStore } from "@/stores/auth";
import type { Response } from '@/types/response'
import type { LoginPayload } from '@/types/payloads/auth'
import TextInput from '@/components/input/TextInput.vue'

const store = useAuthStore();
const toast = useToast();
const router = useRouter();
const route = useRoute()

const props = defineProps({
  redirect: {
    type: String,
    required: false,
    default: "HomeView"
  }
});

const state = reactive({
  username: "",
  password: "",
  rememberMe: false,
});


const createPayload = (): LoginPayload | undefined => {
  if (!state.username) {
    toast.warning('Please enter a username')
    return
  }
  if (!state.password) {
    toast.warning('Please enter a password')
    return
  }
  return {username: state.username, password: state.password, remember_me: state.rememberMe}
}

const loginClicked = () => {
  const payload = createPayload()
  if (payload) {
    store.login(payload).then((response: Response) => {
      toast.success(response.message);
      if (!['RegisterView', 'NotFoundView', 'ForbiddenView', 'UnauthorizedView'].includes(route.name as string)) {
        router.replace({name: props.redirect});
        return
      }
      router.replace({name: 'HomeView'})
    })
  }
};

onMounted(() => {
  if (store.isAuthed) {
    router.replace(props.redirect);
  }
});
</script>
