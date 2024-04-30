<template>
  <div class="menu p-4 bg-base-200 text-base-content justify-between">
    <div>
      <div class="mb-5 text-center" @click="brandClicked">
        <slot name="brand" />
      </div>

      <!-- top -->
      <ul>
        <div
          v-for="(menuItem, index) in props.mainItems"
          :key="index"
          @click="itemClicked(menuItem)"
        >
          <li v-if="showMenuItem(menuItem)">
            <menu-item-component :menu-item="menuItem" />
          </li>
        </div>
      </ul>
    </div>

    <!-- bottom -->
    <ul>
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
</template>

<script setup lang="ts">
import type { PropType } from 'vue';
import { useRouter } from "vue-router";
import type { MenuItem } from "@/types/components/display/navigation";
import MenuItemComponent from './MenuItem.vue'
import { useAuthStore } from '@/stores/auth'
import { useIdentityStore } from '@/stores/auth/identity'

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
  'button-clicked',
  'link-clicked',
  'item-clicked'
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



const brandClicked = () => emit('brand-clicked')

const itemClicked = (item: MenuItem) => {
  emit('item-clicked', item)
  if (item.url) {
    emit('link-clicked', item)
    return
  }
  emit('button-clicked', item)
};
</script>
