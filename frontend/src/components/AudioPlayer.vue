<script setup>
import { ref, useTemplateRef } from "vue";
import PlaybackBar from "./PlaybackBar.vue";
import PlaybackControls from "./PlaybackControls.vue";
import store from "../store";

const props = defineProps(["src"]);

const audio = new Audio(props.src);
const progress = ref(0);
const playbackControls = useTemplateRef("playback-controls");

function syncProgress() {
  progress.value = audio.currentTime / (store.audioDuration / 100);
}

function renderProgress() {
  if (!audio.paused) {
    syncProgress();
    setTimeout(renderProgress, 25);
  } else {
    progress.value = audio.currentTime === audio.duration ? 100 : progress.value;
    if (playbackControls.value) {
      playbackControls.value.isPaused = true;
    } 
  }
}

function onTogglePlayback(isPaused) {
  isPaused ? audio.pause() : audio.play();
  renderProgress();
}

function onRewind(direction) {
  if (direction === "back") {
    audio.currentTime -= 5;
  } else if (direction === "forward") {
    audio.currentTime += 5;
  }
  syncProgress();
}

defineExpose({ audio });
</script>

<template>
  <div class="container">
    <div class="playback-bar-container">
      <PlaybackBar v-bind="{ progress }" />
    </div>
    <PlaybackControls
    ref="playback-controls"
    @toggle-playback="onTogglePlayback"
    @rewind="onRewind" />
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