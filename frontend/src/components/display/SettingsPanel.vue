<template>
  <div class="container mx-auto p-4 border rounded-md">
    <div class="flex justify-between">
      <div class="flex flex-col gap-6">
        <span v-for="setting in props.settings" :key="setting.name"
          >{{ getSettingLabel(setting) }}
          <div
            class="tooltip cursor-pointer ml-2"
            :data-tip="setting.description"
          >
            <i class="fa fa-circle-info" />
          </div>
        </span>
      </div>
      <div class="divider divider-horizontal" />
      <div class="flex flex-col gap-6">
        <input
          v-for="setting in props.settings"
          :key="setting.name"
          :type="getInputType(setting)"
          :class="getInputClass(setting)"
          :value="getInputValue(setting)"
          :checked="getInputChecked(setting)"
          @input="settingUpdated(setting, ($event.target as HTMLInputElement))"
        />
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import type { PropType } from 'vue'
import type { Setting } from '@/types/resources/setting'

const emit = defineEmits(['setting-updated'])

const props = defineProps({
  settings: {
    type: Array as PropType<Setting[]>,
    required: false,
    default: () => []
  }
});

const getSettingLabel = (setting: Setting) => {
  let words = setting.name.toLowerCase().split("_")
  for (let i = 0; i < words.length; i++) {
    words[i] = words[i][0].toUpperCase() + words[i].substr(1);
  }
  return words.join(" ")
}

const getInputType = (setting: Setting) => {
  if (typeof(setting.value) === 'string') {
    return 'text'
  }
  if (typeof(setting.value) === 'number') {
    return 'number'
  }
  if (typeof(setting.value) === 'boolean') {
    return 'checkbox'
  }
}

const getInputClass = (setting: Setting) => {
  if (typeof(setting.value) === 'string') {
    return 'input input-bordered'
  }
  if (typeof(setting.value) === 'number') {
    return 'input input-bordered'
  }
  if (typeof(setting.value) === 'boolean') {
    return 'toggle'
  }
}

const getInputValue = (setting: Setting) => {
  if (typeof(setting.value) === 'string' || typeof(setting.value) === 'number') {
    return setting.value
  }
}

const getInputChecked = (setting: Setting) => {
  if (typeof(setting.value) === 'boolean') {
    return setting.value
  }
}

const settingUpdated = (setting: Setting, value: HTMLInputElement) => {
  if (typeof(setting.value) === 'boolean') {
    setting.value = value.checked
  } else {
    setting.value = value.value
  }
  emit('setting-updated', setting)
}
</script>
