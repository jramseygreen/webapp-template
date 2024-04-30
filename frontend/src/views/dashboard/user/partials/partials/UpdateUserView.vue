<template>
  <div v-if="userStore.user" class="card-body">
    <text-input
      v-model="state.username"
      label="Username"
      placeholder="username"
      :is-required="true"
    />
    <text-input
      v-model="state.newPassword"
      label="New Password"
      type="password"
      placeholder="new password"
    />
    <text-input
      v-model="state.confirmNewPassword"
      label="Confirm New Password"
      type="password"
      placeholder="confirm new password"
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
import type { User } from '@/types/resources/user'
import type { Role } from '@/types/resources/role'
import type { UpdateUserPayload } from '@/types/payloads/user'
import TextInput from '@/components/input/TextInput.vue'
import MultiSelect from '@/components/input/MultiSelect.vue'

const userStore = useUserStore();
const roleStore = useRoleStore();
const router = useRouter()
const toast = useToast()

const props = defineProps({
  id: {
    type: String,
    required: true
  }
});

interface State {
  username: string
  newPassword: string
  confirmNewPassword: string
  isDisabled: boolean
  roles: Role[]
}

const state: State = reactive({
  username: "",
  newPassword: "",
  confirmNewPassword: "",
  isDisabled: false,
  roles: []
});

const createPayload = (): UpdateUserPayload | undefined => {
  let payload: UpdateUserPayload = {
    id: Number(props.id),
    username: state.username,
  }

  if (!state.username) {
    toast.warning("You must enter a username");
    return;
  }
  if (state.newPassword !== state.confirmNewPassword) {
    toast.warning("Passwords must match!");
    return;
  }

  if (state.newPassword) {
    payload.password = state.newPassword
  }

  payload.roles = state.roles.map((role: Role) => role.name)

  return payload
};

const submitClicked = () => {
  const payload = createPayload();
  if (payload) {
    userStore.updateUser(payload).then(response => {
      toast.success(response.message);
      router.push({ name: "UserIndexView" });
    });
  }
};

const setToolBarItems = inject("setToolBarItems") as Function;

onMounted(() => {
    state.username = userStore.user!.username
    state.isDisabled = userStore.user!.is_disabled
    state.roles = userStore.user!.roles!

  roleStore.allRoles()
  setToolBarItems([
    { name: "Back", method: router.back, icon: "fa fa-arrow-left" }
  ]);
});
</script>
