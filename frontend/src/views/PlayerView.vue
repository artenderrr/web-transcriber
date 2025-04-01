<script setup>
import { useTemplateRef } from "vue";
import RestartButton from "../components/RestartButton.vue";
import AudioPlayer from "../components/AudioPlayer.vue";
import store from "../store";

const audioPlayer = useTemplateRef("audio-player");

function pauseAudio() {
  audioPlayer.value.audio.pause();
}
</script>

<template>
  <div class="wrapper">
    <RestartButton @restart="pauseAudio"/>
    <AudioPlayer ref="audio-player" :src="store.audioUrl" />
  </div>
</template>

<style scoped>
.wrapper {
  flex-direction: column;
  gap: 1rem;
}
</style>