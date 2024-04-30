<template>
  <div>
    <top-bar
      class="hidden lg:block"
      :main-items="props.mainItems"
      :secondary-items="props.secondaryItems"
      @item-clicked="itemClicked"
      @brand-clicked="brandClicked"
    >
      <template #brand>
        <slot name="brand" />
      </template>
    </top-bar>

    <div class="drawer lg:hidden">
      <input
        v-model="showSidebar"
        id="sidebar"
        type="checkbox"
        class="drawer-toggle"
      />
      <div class="drawer-content flex justify-between">
        <button
          class="btn btn-ghost rounded-full drawer-button"
          @click="toggleSidebar"
        >
          <i class="fa fa-bars fa-xl" />
        </button>
        <slot name="brand" />
        <div />
      </div>
      <div class="drawer-side z-50">
        <label
          for="sidebar"
          aria-label="close sidebar"
          class="drawer-overlay"
        />
        <side-bar
          class="w-80 h-full"
          :main-items="props.mainItems"
          :secondary-items="props.secondaryItems"
          @item-clicked="itemClicked"
          @brand-clicked="brandClicked"
        >
          <template #brand>
            <slot name="brand" />
          </template>
        </side-bar>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from "vue-router";
import type { PropType } from 'vue';
import type { MenuItem } from "@/types/components/display/navigation";
import TopBar from "./TopBar.vue";
import SideBar from "./SideBar.vue";

const router = useRouter();

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
  'item-clicked',
  'button-clicked',
  'link-clicked',
  'brand-clicked'
])

const showSidebar = ref(false)

const toggleSidebar = () => {
  showSidebar.value = !showSidebar.value
}

const brandClicked = () => {
  showSidebar.value = false;
  emit('brand-clicked');
}

const itemClicked = (menuItem: MenuItem) => {
  showSidebar.value = false;
  emit('item-clicked', menuItem)
  if (menuItem.url) {
    emit('link-clicked', menuItem)
    return
    }
  emit('button-clicked', menuItem)
}
</script>
