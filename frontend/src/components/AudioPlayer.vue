<script setup>
import PlaybackBar from "./PlaybackBar.vue";
import PlaybackControls from "./PlaybackControls.vue";

const props = defineProps(["src"]);

const audio = new Audio(props.src);

function onTogglePlayback(isPaused) {
  isPaused ? audio.pause() : audio.play();
}
</script>

<template>
  <div class="container">
    <div class="playback-bar-container">
      <PlaybackBar :progress="20" />
    </div>
    <PlaybackControls @toggle-playback="onTogglePlayback" />
  </div>
</template>

<style scoped>
.container {
  background-color: #2b2b2b;
  
  width: 20rem;
  height: 10rem;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  border: .125rem solid #3b3b3b;
  border-radius: 1.5rem;

  padding: 1rem;
}

.playback-bar-container {
  width: 100%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}
</style>