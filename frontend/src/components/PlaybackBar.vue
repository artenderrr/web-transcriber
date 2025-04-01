<script setup>
defineProps(["progress"]);
</script>

<template>
  <div class="playback-bar">
    <div class="playback-progress" :style="{ width: progress + '%' }"></div>
  </div>
</template>

<style scoped>
.playback-bar {
  background-color: #3b3b3b;

  width: 100%;
  height: 1rem;

  border-radius: .5rem;

  overflow: hidden;
}

.playback-progress {
  background-color: #5b5b5b;

  height: 100%;
}
</style>