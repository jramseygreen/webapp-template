<template>
  <div class="form-control">
    <label class="label">
      <span v-if="props.label" class="label-text">{{ props.label }}</span>
      <i
        v-if="props.isRequired"
        class="label-text text-red-500 fa fa-asterisk fa-2xs"
      />
    </label>
    <input
      class="input input-bordered"
      :value="props.modelValue"
      :type="props.type"
      :placeholder="props.placeholder"
      :disabled="props.isDisabled"
      @input="modelValueUpdated"
    />
  </div>
</template>
<script setup lang="ts">
const emit = defineEmits(["update:modelValue"]);

const props = defineProps({
  modelValue: {
    type: String,
    required: false,
    default: ""
  },
  label: {
    type: String,
    required: false
  },
  type: {
    type: String,
    required: false,
    default: "text"
  },
  placeholder: {
    type: String,
    required: false,
    default: ""
  },
  isRequired: {
    type: Boolean,
    required: false,
    default: false
  },
  isDisabled: {
    type: Boolean,
    required: false,
    default: false
  }
});

const modelValueUpdated = (event: Event) => {
  emit("update:modelValue", (event.target as HTMLInputElement)?.value);
};
</script>
