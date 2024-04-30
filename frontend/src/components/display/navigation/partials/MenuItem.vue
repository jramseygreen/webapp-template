<template>
  <component
    :is="props.menuItem.url ? 'router-link' : 'button'"
    :to="props.menuItem.url"
    class="mr-1"
    :class="classes"
    @click="menuItemClicked"
  >
    <i v-if="props.menuItem.icon" :class="props.menuItem.icon" class="mr-1" />
    {{ props.menuItem.name }}
  </component>
</template>
<script setup lang="ts">
import type { PropType } from 'vue'
import type { MenuItem } from "@/types/components/display/navigation";
import { computed } from 'vue'

const props = defineProps({
  menuItem: {
    type: Object as PropType<MenuItem>,
    required: true
  },
  class: {
    type: String,
    required: false,
    default: 'btn btn-ghost'
  }
});

const menuItemClicked = () => {
  if (props.menuItem.method) {
    props.menuItem.method(props.menuItem)
  }
}

const classes = computed(() => {
  let classes = props.class
  if (props.menuItem.isDisabled) {
    classes += ' btn-disabled'
  }
  return classes
})
</script>
