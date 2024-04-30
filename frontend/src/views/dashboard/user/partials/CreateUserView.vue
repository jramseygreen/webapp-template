<template>
  <div class="card-body">
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
    <div class="form-control flex align-items-center gap-2">
      <span class="label-text">Disabled</span>
      <input v-model="state.isDisabled" type="checkbox" class="checkbox" />
    </div>
    <multi-select
      v-model="state.roles"
      :selections="roleStore.roles"
      label="Select User Roles"
    />
    <div class="form-control mt-6">
      <button class="btn btn-primary" @click="submitClicked">Submit</button>
    </div>
  </div>
</template>
<script setup lang="ts">
import { onMounted, inject, reactive } from "vue";
import { useUserStore } from "@/stores/user";
import { useRoleStore } from "@/stores/role";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import type { CreateUserPayload } from '@/types/payloads/user'
import type { Role } from '@/types/resources/role'
import type { Response } from '@/types/response'
import TextInput from '@/components/input/TextInput.vue'
import MultiSelect from '@/components/input/MultiSelect.vue'

const userStore = useUserStore();
const roleStore = useRoleStore();
const router = useRouter()
const toast = useToast()

const setToolBarItems = inject("setToolBarItems") as Function;

interface State {
  username: string
  password: string
  confirmPassword: string
  isDisabled: boolean
  roles: Role[]
}

const state: State = reactive({
  username: "",
  password: "",
  confirmPassword: "",
  isDisabled: false,
  roles: []
});

const createPayload = (): CreateUserPayload | undefined => {
  if (!state.username) {
    toast.warning("You must enter a username");
    return;
  }
  if (!state.password) {
    toast.warning("You must enter a password");
    return;
  }
  if (state.password !== state.confirmPassword) {
    toast.warning("Passwords must match!");
    return;
  }

  return {
    username: state.username,
    password: state.password,
    is_disabled: state.isDisabled,
    roles: state.roles.map((role: Role) => role.name)
  };
};

const submitClicked = () => {
  const payload = createPayload();
  if (payload) {
    userStore.createUser(payload).then(response => {
      toast.success(response.message);
      router.push({ name: "AllUsersView" });
    });
  }
};

onMounted(() => {
  roleStore.allRoles()
  setToolBarItems([
    { name: "Back", method: router.back, icon: "fa fa-arrow-left" }
  ]);
});
</script>
