<template>
  <settings-panel
    v-if="store.settings"
    :settings="store.settings"
    @setting-updated="settingUpdated"
  />
</template>
<script setup lang="ts">
import { onMounted, inject, reactive, computed } from "vue";
import { useSettingStore } from "@/stores/setting";
import SettingsPanel from "@/components/display/SettingsPanel.vue";
import type { Setting } from '@/types/resources/setting'
import { useToast } from 'vue-toastification'

const store = useSettingStore();
const toast = useToast()
const setToolBarItems = inject("setToolBarItems") as Function;

const toolbarItems = computed(() => [
    {
      name: "Save",
      method: saveClicked,
      icon: "fa fa-floppy-disk",
      isDisabled: !payload.settings.length
    }
  ])

const payload = reactive({
  settings: [] as Setting[]
});

const settingUpdated = (setting: Setting) => {
  const index = payload.settings.findIndex(s => s.name === setting.name);
  if (index !== -1) {
    // If setting with the same name already exists, update its value
    payload.settings[index].value = setting.value;
    if (store.settings.includes(setting)) {
      // remove setting from payload
      payload.settings.splice(index, 1)
    }
  } else {
    // If setting doesn't exist, append it to the array
    payload.settings.push(setting);
  }

  setToolBarItems(toolbarItems)
}

const saveClicked = () => {
  store.updateAllSettings(payload).then((response) => {
    payload.settings = []
    toast.success(response.message);
  })
};

onMounted(() => {
  store.allSettings()
  setToolBarItems(toolbarItems)
});
</script>
