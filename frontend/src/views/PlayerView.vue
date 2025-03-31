<script setup>
import RestartButton from "../components/RestartButton.vue";
import store from "../store";
</script>

<template>
  <div class="wrapper">
    <RestartButton />
    <audio v-if="store.audioUrl" :src="store.audioUrl" controls></audio>
  </div>
</template>

<style scoped>
.wrapper {
  flex-direction: column;
  gap: 1rem;
}
</style>