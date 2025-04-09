<script setup>
import { computed } from "vue";

const props = defineProps(["progress"]);
const progress = computed(() => props.progress || 0);
</script>

<template>
  <div class="progress-bar-container">
    <div class="progress-bar-value" :style="{ width: progress + '%' }"></div>
  </div>
</template>

<style scoped>
.progress-bar-container {
  background-color: #2b2b2b;

  width: 20rem;
  height: 1rem;

  border-radius: .75rem;

  overflow: hidden;
}

.progress-bar-value {
  background-color: #5b5b5b;

  height: 100%;

  transition: width .125s;
}
</style>