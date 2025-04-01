<script setup>
import { useTemplateRef } from "vue";

defineProps(["progress"]);

const emit = defineEmits(["set-progress"]);

const playbackBar = useTemplateRef("playback-bar");

function onClick(event) {
  const playbackBarRect = playbackBar.value.getBoundingClientRect();
  const x = event.x - playbackBarRect.x;
  const newProgress = x / (playbackBarRect.width / 100);

  emit("set-progress", newProgress);
}
</script>

<template>
  <div ref="playback-bar" class="playback-bar" @click="onClick">
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

  cursor: pointer;
}

.playback-progress {
  background-color: #5b5b5b;

  height: 100%;

  transition: width .125s;
}
</style>