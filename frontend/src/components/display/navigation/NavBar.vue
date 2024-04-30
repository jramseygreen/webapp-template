<template>
  <div>
    <combined-bar
      :main-items="state.mainItems"
      :secondary-items="state.secondaryItems"
      @button-clicked="buttonClicked"
    >
      <template #brand>
        <router-link :to="{ name: 'HomeView' }" class="btn normal-case text-xl"
          >App Brand</router-link
        >
      </template>
    </combined-bar>
  </div>
</template>
<script setup lang="ts">
import { reactive, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useToast } from 'vue-toastification'
import type { MenuItem } from "@/types/components/display/navigation";
import CombinedBar from './partials/CombinedBar.vue'
import { useAuthStore } from '@/stores/auth'
import { useSettingStore } from '@/stores/setting'

const authStore = useAuthStore()
const settingStore = useSettingStore()
const router = useRouter()
const route = useRoute()
const toast = useToast()

const secondaryItems = computed((): MenuItem[] => {
  let items = [{ name: "Login", showWithAuthentication: false }] as MenuItem[]
  if (settingStore.isRegistrationEnabled) {
    items.push({ name: "Register", url: { name: "RegisterView" }, showWithAuthentication: false })
  }
  items.push(
    { name: "Dashboard", url: { name: "DashboardView" }, showWithAuthentication: true },
    { name: "Logout", showWithAuthentication: true }
  )
  return items
})

const state = reactive({
  mainItems: [
    { name: "Page One", url: {name: 'PageOneView'} },
    { name: "Page Two", url: {name: 'PageTwoView'} }
  ] as MenuItem[],
  secondaryItems: secondaryItems
});

const buttonClicked = (menuItem: MenuItem) => {
  switch (menuItem.name) {
    case 'Login':
      router.push({name: 'LoginView', query: {redirect: route.name as string}})
      break;
    case "Logout":
      authStore.logout();
      router.push({ name: "HomeView" });
      toast.success('Logged out successfully')
      break;
  }
};
</script>
