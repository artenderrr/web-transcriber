<script setup>
import { ref } from "vue";

const emit = defineEmits(["toggle-playback", "rewind"]);

const isPaused = ref(true);

function togglePlayback() {
  isPaused.value = !isPaused.value;
  emit("toggle-playback", isPaused.value);
}

defineExpose({ isPaused });
</script>

<template>
  <div class="controls-wrapper">
    <svg class="rewind-control" @click="$emit('rewind', 'back')" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path d="M15 18a6 6 0 1 0 0-12H4"/><path d="M7 9L4 6l3-3m1 17h2a1 1 0 0 0 1-1v-1a1 1 0 0 0-1-1H8v-3h3"/></g></svg>
    <div @click="togglePlayback">
      <svg v-if="isPaused" class="playback-toggle" xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24"><path fill="currentColor" d="M21.409 9.353a2.998 2.998 0 0 1 0 5.294L8.597 21.614C6.534 22.737 4 21.277 4 18.968V5.033c0-2.31 2.534-3.769 4.597-2.648z"/></svg>
      <svg v-else class="playback-toggle" xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24"><path fill="currentColor" d="M2 6c0-1.886 0-2.828.586-3.414S4.114 2 6 2s2.828 0 3.414.586S10 4.114 10 6v12c0 1.886 0 2.828-.586 3.414S7.886 22 6 22s-2.828 0-3.414-.586S2 19.886 2 18zm12 0c0-1.886 0-2.828.586-3.414S16.114 2 18 2s2.828 0 3.414.586S22 4.114 22 6v12c0 1.886 0 2.828-.586 3.414S19.886 22 18 22s-2.828 0-3.414-.586S14 19.886 14 18z"/></svg>
    </div>
    <svg class="rewind-control" @click="$emit('rewind', 'forward')" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path d="M9 18A6 6 0 1 1 9 6h11m-7 14h2a1 1 0 0 0 1-1v-1a1 1 0 0 0-1-1h-2v-3h3"/><path d="m17 9l3-3l-3-3"/></g></svg>
  </div>
</template>

<style scoped>
.controls-wrapper {
  color: #5b5b5b;

  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
  gap: .5rem;
}

svg {
  display: block;

  cursor: pointer;
}

.playback-toggle {
  width: 5rem;
  height: 5rem;
}

.rewind-control {
  width: 3.5rem;
  height: 3.5rem;
}
</style>