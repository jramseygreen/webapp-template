<template>
  <div class="flex flex-col lg:flex-row lg:h-full">
    <side-bar class="lg:w-80" :main-items="state.menuItems" />
    <div class="p-2 w-full flex flex-col">
      <tool-bar
        :title="state.toolBarTitle"
        :subtitle="state.toolBarSubtitle"
        :items="state.toolBarItems"
      />
      <router-view />
    </div>
  </div>
</template>

<script setup lang="ts">
import { provide, reactive } from "vue";
import SideBar from "@/components/display/navigation/partials/SideBar.vue";
import type { MenuItem } from "@/types/components/display/navigation"
import ToolBar from '@/components/display/navigation/ToolBar.vue'


interface State {
  menuItems: MenuItem[]
  toolBarItems: MenuItem[]
  toolBarSubtitle: string
  toolBarTitle: string
}

const state: State = reactive({
  menuItems: [
    { name: "Profile", url: { name: "ProfileIndexView" } },
    { name: "Roles", url: { name: "RolesIndexView" }, allows: ["admin"] },
    { name: "Users", url: { name: "UsersIndexView" }, allows: ["admin"] },
    { name: "Settings", url: { name: "SettingsIndexView" }, allows: ["admin"] }
  ],
  toolBarItems: [],
  toolBarSubtitle: '',
  toolBarTitle: ''
})

const setToolBarItems = (items: MenuItem[]) => {
  state.toolBarItems = items
}

const setToolBarTitle = (title: string) => {
  state.toolBarTitle = title
}

const setToolBarSubtitle = (subtitle: string) => {
  state.toolBarSubtitle = subtitle
}

provide('setToolBarItems', setToolBarItems)
provide('setToolBarSubtitle', setToolBarSubtitle)
provide('setToolBarTitle', setToolBarTitle)
</script>
