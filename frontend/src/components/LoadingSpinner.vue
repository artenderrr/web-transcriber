<template>
  <svg class="loading-spinner" viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg">
    <circle cx="400" cy="400" fill="none"
      r="300" stroke-width="115" stroke="#5b5b5b"
      stroke-dasharray="1350 1400"
      stroke-linecap="round" />
  </svg>
</template>

<style scoped>
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.loading-spinner {
  animation: spin 2s linear infinite;
}
</style>