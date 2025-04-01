<script setup>
import RestartButton from "../components/RestartButton.vue";
import AudioPlayer from "../components/AudioPlayer.vue";
import store from "../store";
</script>

<template>
  <div class="wrapper">
    <RestartButton />
    <AudioPlayer :src="store.audioUrl" />
  </div>
</template>

<style scoped>
.wrapper {
  flex-direction: column;
  gap: 1rem;
}
</style>