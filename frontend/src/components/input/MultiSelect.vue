<template>
  <div class="form-control">
    <label class="label">
      <span v-if="props.label" class="label-text">{{ props.label }}</span>
      <i
        v-if="props.isRequired"
        class="label-text text-red-500 fa fa-asterisk fa-2xs"
      />
    </label>
    <div
      tabindex="-1"
      class="w-full"
      :class="props.isDisabled ? 'cursor-not-allowed' : ''"
      @blur="elementUnfocused('div')"
      @focus="elementFocused('div')"
    >
      <div class="input input-bordered flex justify-between items-center">
        <!-- Selected Items -->
        <div class="flex gap-1 w-full">
          <div
            v-for="selectedItem in state.selectedItems"
            :key="selectedItem.id as number"
            class="group badge badge-secondary badge-outline cursor-pointer"
            @click="selectedItemClicked(selectedItem)"
          >
            {{ selectedItem.name }}
            <i
              class="text-white fa fa-xmark fa-xs ml-1 hidden group-hover:block"
            />
          </div>
          <div
            v-if="state.selectedItems.length"
            class="border-l border-gray-600 mx-1"
          />
          <input
            v-model="state.searchString"
            class="w-full bg-base-100"
            :class="{ 'cursor-not-allowed': props.isDisabled }"
            type="text"
            :placeholder="props.placeholder"
            :disabled="props.isDisabled"
            @keyup.enter="searchSubmit"
            @blur="elementUnfocused('search')"
            @focus="elementFocused('search')"
          />
        </div>
        <!-- Toggle Icon -->
        <div v-if="!props.isDisabled" class="cursor-pointer">
          <div v-if="state.isOpen" tabindex="0" @focus.prevent="toggleOpen">
            <i class="fa fa-chevron-up" />
          </div>
          <div v-else tabindex="0" @focus.prevent="toggleOpen">
            <i class="fa fa-chevron-down" />
          </div>
        </div>
      </div>
      <!-- Dropdown -->
      <div class="dropdown w-full" :class="{ 'dropdown-open': state.isOpen }">
        <div
          class="dropdown-content menu rounded-box shadow bg-base-200 z-[1] w-full"
        >
          <ul>
            <li
              v-for="selection in remainingSelections"
              :key="selection.id as number"
              class="text-base rounded cursor-pointer p-1 hover:bg-base-300"
              @click="selectionClicked(selection)"
            >
              {{ selection[props.displayKey] }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, watch, computed, defineEmits, defineProps } from 'vue'
import type { PropType } from 'vue'
import type { SelectItem } from '@/types/components/input/multiSelect'

const emit = defineEmits(['update:modelValue'])

const props = defineProps({
  modelValue: { type: Array as PropType<SelectItem[]>, required: false, default: () => [] },
  selections: { type: Array as PropType<SelectItem[]>, required: false, default: () => [] },
  isRequired: { type: Boolean, required: false, default: false },
  isDisabled: { type: Boolean, required: false, default: false },
  label: { type: String, required: false },
  placeholder: { type: String, required: false, default: "Type to search or add selection" },
  displayKey: { type: String, required: false, default: "name" },
})

const state = reactive({
  selectedItems: props.modelValue,
  isOpen: false,
  divFocused: false,
  searchFocused: false,
  searchString: ''
})

const remainingSelections = computed(() => props.selections.filter(
  (selection: SelectItem) =>
    !state.selectedItems.includes(selection) &&
    selection[props.displayKey].includes(state.searchString)
))

const elementFocused = (element: string) => {
  if (!props.isDisabled) {
    state.isOpen = true
    state.divFocused = element === 'div'
    state.searchFocused = element === 'search'
  }
}

const elementUnfocused = (element: string) => {
  state.divFocused = state.searchFocused = false
  if (!state.divFocused && !state.searchFocused) state.isOpen = false
}

const toggleOpen = () => {
  state.isOpen = !state.isOpen
}

const searchSubmit = () => {
  if (remainingSelections.value.length && state.searchString) {
    selectionClicked(remainingSelections.value[0])
    state.searchString = ''
  }
}

const selectionClicked = (selection: SelectItem) => {
  state.selectedItems.push(selection)
  emit('update:modelValue', state.selectedItems)
}

const selectedItemClicked = (selection: SelectItem) => {
  state.selectedItems = state.selectedItems.filter((item: SelectItem) => item !== selection)
  emit('update:modelValue', state.selectedItems)
}

watch(() => props.modelValue, () => {
  if (state.selectedItems !== props.modelValue) state.selectedItems = props.modelValue
})
</script>
