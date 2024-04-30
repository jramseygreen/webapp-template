<template>
  <data-grid class="h-full" :columns="processedColumns" :records="props.roles">
    <template #name="{record}">
      <component
        :is="store.hasRole('admin') ? 'router-link' : 'div'"
        :to="{ name: 'ReadRoleView', params: { id: record.id } }"
        class="badge badge-primary badge-outline"
      >
        {{ record.name }}
      </component>
    </template>

    <template #actions="{record}">
      <div class="flex gap-1">
        <div class="tooltip" data-tip="Update">
          <router-link
            :to="{ name: 'UpdateRoleView', params: { id: record.id } }"
            class="btn btn-neutral btn-xs"
            :class="record.name === 'admin' ? 'btn-disabled' : ''"
          >
            <i class="fa fa-pen-to-square" />
          </router-link>
        </div>
        <div class="tooltip" data-tip="Delete">
          <router-link
            :to="{ name: 'DeleteRoleView', params: { id: record.id } }"
            class="btn btn-neutral btn-xs"
            :class="record.name === 'admin' ? 'btn-disabled' : ''"
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
import type { Role } from '@/types/resources/role'
import type { PropType } from 'vue'
import type { Column } from '@/types/components/display/dataGrid'
import { useIdentityStore } from "@/stores/auth/identity";

const store = useIdentityStore()

const props = defineProps({
  roles: {
    type: Array as PropType<Role[]>,
    required: false,
    default: () => []
  },
  columns: {
    type: Array as PropType<Column[]>,
    required: false,
    default: () => [
      { name: 'id', key: 'id' },
      { name: 'name', key: 'name' },
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
