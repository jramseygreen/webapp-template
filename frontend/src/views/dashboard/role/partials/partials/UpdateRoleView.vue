<template>
  <div v-if="store.role" class="card-body">
    <text-input
      v-model="state.role"
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
import type { Role } from '@/types/resources/role'
import type { UpdateRolePayload } from '@/types/payloads/role'
import TextInput from '@/components/input/TextInput.vue'

const store = useRoleStore();
const router = useRouter()
const toast = useToast()

const props = defineProps({
  id: {
    type: String,
    required: true
  }
});

interface State {
  role: string
}

const state: State = reactive({
  role: "",
});


const createPayload = (): UpdateRolePayload | undefined => {
  if (!state.role) {
    toast.warning("You must enter a role name");
    return;
  }

  return {
    id: Number(props.id),
    name: state.role,
  }
};

const submitClicked = () => {
  const payload = createPayload();
  if (payload) {
    store.updateRole(payload).then(response => {
      toast.success(response.message);
      router.push({ name: "RoleIndexView" });
    });
  }
};

const setToolBarItems = inject("setToolBarItems") as Function;

onMounted(() => {
  state.role = store.role!.name
  setToolBarItems([
    { name: "Back", method: router.back, icon: "fa fa-arrow-left" }
  ]);
});
</script>
