<script setup>
import LoadingSpinner from "../components/LoadingSpinner.vue";
</script>

<template>
  <div class="wrapper">
    <LoadingSpinner class="loading-spinner" />
    <div class="transcription-text-container">
      <span class="upper-text">Переводим в текст.</span>
      <span>Пожалуйста, подождите...</span>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  flex-direction: column;
  gap: 1.25rem;

  color: #5b5b5b;
}

.loading-spinner {
  width: 4.5rem;
}

.transcription-text-container {
  font-size: 1.75rem;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.upper-text {
  color: #424242;
}
</style>