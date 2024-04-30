<template>
  <data-grid class="h-full" :columns="processedColumns" :records="props.users">
    <template #username="{record}">
      <router-link
        :to="{ name: 'ReadUserView', params: { id: record.id } }"
        class="border-b"
      >
        {{ record.username }}
      </router-link>
    </template>

    <template #roles="{record}">
      <div v-if="!record.roles.length" />
      <router-link
        v-for="role in record.roles"
        :key="role.id"
        :to="{ name: 'ReadRoleView', params: { id: record.id } }"
        class="badge badge-primary badge-outline mx-1"
      >
        {{ role.name }}
      </router-link>
    </template>

    <template #actions="{record}">
      <div class="flex gap-1">
        <div class="tooltip" data-tip="Update">
          <router-link
            :to="{ name: 'UpdateUserView', params: { id: record.id } }"
            class="btn btn-neutral btn-xs"
          >
            <i class="fa fa-pen-to-square" />
          </router-link>
        </div>
        <div class="tooltip" data-tip="Delete">
          <router-link
            :to="{ name: 'DeleteUserView', params: { id: record.id } }"
            class="btn btn-neutral btn-xs"
          >
            <i class="fa fa-trash-can" />
          </router-link>
        </div>
      </div>
    </template>
  </data-grid>
</template>
<script setup lang="ts">
import { onMounted, computed } from "vue";
import DataGrid from "@/components/display/DataGrid.vue";
import type { User } from '@/types/resources/user'
import type { PropType } from 'vue'
import type { Column } from '@/types/components/display/dataGrid'

const props = defineProps({
  users: {
    type: Array as PropType<User[]>,
    required: false,
    default: () => []
  },
  columns: {
    type: Array as PropType<Column[]>,
    required: false,
    default: () => [
      { name: 'id', key: 'id' },
      { name: 'username', key: 'username' },
      { name: 'disabled', key: 'is_disabled' },
      { name: 'roles', key: 'roles' },
      { name: 'actions' }
    ]
  },
  excludeColumns: {
    type: Array as PropType<string[]>,
    required: false,
    default: () => []
  }
});

const processedColumns = computed(() => props.columns.filter((column: Column) => !props.excludeColumns.includes(column.name)))
</script>
