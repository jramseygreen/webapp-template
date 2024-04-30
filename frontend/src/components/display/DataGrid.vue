<template>
  <div class="overflow-auto">
    <table class="table table-pin-rows">
      <thead>
        <tr>
          <th
            v-for="column in props.columns"
            :key="column.key ? column.key : column.name"
          >
            {{ column.name }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr class="hover" v-for="record in props.records" :key="record.id">
          <td
            v-for="column in props.columns"
            :key="column.key ? column.key : column.name"
          >
            <slot :name="column.name" :record="record">
              <div v-if="column.key && column.key in record">
                {{ record[column.key] }}
              </div>
              <div v-else-if="column.name && column.name in record">
                {{ record[column.name] }}
              </div>
            </slot>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <span v-if="!props.records.length" class="text-center w-full"
    >No records to show...</span
  >
</template>

<script setup lang="ts">
import type { PropType } from 'vue'
import type { Column } from '@/types/components/display/dataGrid'
import type { Record } from '@/types/components/display/dataGrid'

const props = defineProps({
  columns: {
    type: Array as PropType<Column[]>,
    required: false,
    default: () => []
  },
  records: {
    type: Array as PropType<Record[]>,
    required: false,
    default: () => []
  }
});
</script>
