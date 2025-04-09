<script setup>
import { computed } from "vue";

const props = defineProps(["progress"]);
const progress = computed(() => props.progress || 0);
</script>

<template>
  <div class="progress-number-container">
    <span>{{ progress }}</span>
    <span>%</span>
  </div>
</template>

<style scoped>
.progress-number-container {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  gap: .125rem;
}

.progress-number-container > span:first-of-type {
  font-size: 5rem;
  line-height: 1.05;
}

.progress-number-container > span:last-of-type {
  color: #424242;
  font-size: 3.5rem;
}
</style>