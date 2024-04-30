<template>
  <div class="card-body">
    <text-input
      v-model="state.name"
      label="Role Name"
      placeholder="role name"
      :is-required="true"
    />

    <div class="form-control mt-6">
      <button class="btn btn-primary" @click="submitClicked">Submit</button>
    </div>
  </div>
</template>
<script setup lang="ts">
import { onMounted, inject, reactive } from "vue";
import { useRoleStore } from "@/stores/role";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import type { CreateRolePayload } from '@/types/payloads/role'
import type { Role } from '@/types/resources/role'
import type { Response } from '@/types/response'
import TextInput from '@/components/input/TextInput.vue'

const store = useRoleStore();
const router = useRouter()
const toast = useToast()

const setToolBarItems = inject("setToolBarItems") as Function;

interface State {
  name: string
}

const state: State = reactive({
  name: "",
});

const createPayload = (): CreateRolePayload | undefined => {
  if (!state.name) {
    toast.warning("You must enter a role name");
    return;
  }

  return {
    name: state.name
  };
};

const submitClicked = () => {
  const payload = createPayload();
  if (payload) {
    store.createRole(payload).then((response: Response<Role>) => {
      toast.success(response.message);
      router.push({ name: "RolesIndexView" });
    });
  }
};

onMounted(() => {
  setToolBarItems([
    { name: "Back", method: router.back, icon: "fa fa-arrow-left" }
  ]);
});
</script>
