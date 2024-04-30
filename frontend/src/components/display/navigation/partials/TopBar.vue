<template>
  <div class="navbar bg-base-100">
    <div class="flex justify-between">
      <!-- left -->
      <div class="flex">
        <div class="mr-8" @click="brandClicked">
          <slot name="brand" />
        </div>
        <div
          v-for="(menuItem, index) in props.mainItems"
          :key="index"
          @click="itemClicked(menuItem)"
        >
          <div v-if="showMenuItem(menuItem)" class="mr-3">
            <menu-item-component :menu-item="menuItem" />
          </div>
        </div>
      </div>

      <!-- right -->
      <div v-if="props.secondaryItems.length" class="dropdown dropdown-end">
        <label tabindex="0" class="btn btn-ghost rounded-full m-1"
          ><i class="fa fa-user"
        /></label>
        <ul
          tabindex="0"
          class="p-2 shadow menu dropdown-content z-[2] bg-base-200 rounded-box w-52"
        >
          <div
            v-for="(menuItem, index) in props.secondaryItems"
            :key="index"
            @click="itemClicked(menuItem)"
          >
            <li v-if="showMenuItem(menuItem)">
              <menu-item-component :menu-item="menuItem" />
            </li>
          </div>
        </ul>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import type { PropType } from 'vue';
import { useRouter } from "vue-router";
import type { MenuItem } from "@/types/components/display/navigation";
import { useAuthStore } from '@/stores/auth'
import { useIdentityStore } from '@/stores/auth/identity'
import MenuItemComponent from './MenuItem.vue'

const authStore = useAuthStore()
const identityStore = useIdentityStore()

const props = defineProps({
  mainItems: {
    type: Array as PropType<MenuItem[]>,
    required: false,
    default: () => []
  },
  secondaryItems: {
    type: Array as PropType<MenuItem[]>,
    required: false,
    default: () => []
  },
})

const emit = defineEmits([
  'brand-clicked',
  'item-clicked',
  'button-clicked',
  'link-clicked'
])

const router = useRouter();


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

const brandClicked = () => {
  emit('brand-clicked')
}

const itemClicked = (item: MenuItem) => {
  emit('item-clicked', item)
  if (item.url) {
    emit('link-clicked', item)
    return
  }
  emit('button-clicked', item)
};
</script>
