<script setup>
import { ref } from "vue";

const isRecording = ref(false);
</script>

<template>
  <button @click="isRecording = !isRecording">
    <div class="circle">
      <div class="circle" :class="{ pulsing: isRecording }"></div>
    </div>
    <span>{{ !isRecording ? "Начать запись" : "Закончить запись" }}</span>
  </button>
</template>

<style scoped>
button {
  background-color: #2b2b2b;
  color: #cdcdcd;

  font: inherit;

  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;

  border: .125rem solid #3b3b3b;
  border-radius: 1rem;

  padding: 1rem;
  padding-inline: 1.5rem;

  cursor: pointer;
}

.circle {
  background-color: crimson;

  width: 1.25rem;
  aspect-ratio: 1 / 1;

  border-radius: 50%;
}

.pulsing {
  animation: pulse 1s ease infinite;
}

@keyframes pulse {
  to {
    transform: scale(1.75);
    opacity: 0;
  }
}
</style>