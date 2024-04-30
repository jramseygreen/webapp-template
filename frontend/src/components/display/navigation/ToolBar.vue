<template>
  <div class="flex justify-between">
    <div class="flex items-center mb-5">
      <h1 class="text-5xl font-bold">{{ props.title }}</h1>
      <h2 v-if="props.subtitle" class="text-2xl font-bold ml-2">
        - {{ props.subtitle }}
      </h2>
    </div>
    <div class="flex gap-2">
      <div
        v-for="menuItem in props.items"
        :key="menuItem.name"
        @click="itemClicked(menuItem)"
      >
        <menu-item-component
          v-if="showMenuItem(menuItem)"
          class="btn btn-neutral"
          :menu-item="menuItem"
        />
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import type { MenuItem } from "@/types/components/display/navigation"
import type { PropType } from 'vue'
import MenuItemComponent from '@/components/display/navigation/partials/MenuItem.vue'
import { useAuthStore } from '@/stores/auth'
import { useIdentityStore } from '@/stores/auth/identity'


const authStore = useAuthStore()
const identityStore = useIdentityStore()

const emit = defineEmits(['item-clicked', 'link-clicked', 'button-clicked'])

const props = defineProps({
  title: {
    type: String,
    required: false,
    default: ''
  },
  subtitle: {
    type: String,
    required: false
  },
  items: {
    type: Array as PropType<MenuItem[]>,
    required: false,
    default: () => []
  }
})

const itemClicked = (item: MenuItem) => {
  emit('item-clicked', item)
  if (item.url) {
    emit('link-clicked', item)
    return
  }
  emit('button-clicked', item)
};

const showMenuItem = (menuItem: MenuItem) => {
  const authCheck = menuItem.showWithAuthentication === undefined || authStore.isAuthed === menuItem.showWithAuthentication;
  let allowsCheck = true
  if (menuItem.allows) {
    allowsCheck = menuItem.allows.some((role: string) => identityStore.hasRole(role))
  }
  let blocksCheck = true
  if (menuItem.blocks) {
    blocksCheck = menuItem.blocks.every((role: string) => !identityStore.hasRole(role))
  }
  return authCheck && allowsCheck && blocksCheck
};
</script>
