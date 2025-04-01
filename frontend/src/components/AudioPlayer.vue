<script setup>
import { ref, useTemplateRef } from "vue";
import PlaybackBar from "./PlaybackBar.vue";
import PlaybackControls from "./PlaybackControls.vue";

const props = defineProps(["src"]);

const audio = new Audio(props.src);
const progress = ref(0);
const playbackControls = useTemplateRef("playback-controls");

function renderProgress() {
  if (!audio.paused) {
    progress.value = audio.currentTime / (audio.duration / 100);
    setTimeout(renderProgress, 500);
  } else {
    playbackControls.value.isPaused = true;
  }
}

function onTogglePlayback(isPaused) {
  isPaused ? audio.pause() : audio.play();
  renderProgress();
}
</script>

<template>
  <div class="container">
    <div class="playback-bar-container">
      <PlaybackBar v-bind="{ progress }" />
    </div>
    <PlaybackControls ref="playback-controls" @toggle-playback="onTogglePlayback" />
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