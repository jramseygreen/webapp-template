<template>
  <error-template :title="props.title" :description="props.description">
    <template v-if="!store.isAuthed" #content>
      <div class="flex justify-between">
        <router-link :to="{ name: 'HomeView' }" class="btn btn-primary"
          ><i class="fas fa-home" /> Go Home</router-link
        >
        <router-link
          :to="{ name: 'LoginView', query: { redirect: props.redirect } }"
          class="btn btn-primary"
          ><i class="fas fa-right-to-bracket" />Go to Login</router-link
        >
      </div>
    </template>
  </error-template>
</template>

<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import { computed } from "vue";
import ErrorTemplate from "@/components/display/errors/ErrorTemplate.vue";

const store = useAuthStore();

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  redirect: {
    type: String,
    required: false
  }
});
</script>
