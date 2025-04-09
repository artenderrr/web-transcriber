<script setup>
import router from "../router";
import store from "../store";
</script>

<template>
  <div class="wrapper">
    <button @click="router.back()">
      <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.35" d="m9 11l-4 4l4 4m-4-4h11a4 4 0 0 0 0-8h-1"/></svg>
    </button>
    <div class="outer-transcription-container">
      <div class="inner-transcription-container">
        <p v-if="store.transcriptionText">{{ store.transcriptionText }}</p>
        <p v-else class="transcription-text-fallback">Речь не распознана.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  flex-direction: column;
  gap: 1.5rem;
}

button {
  background-color: #2b2b2b;
  color: #5b5b5b;

  width: 5rem;
  aspect-ratio: 1 / 1;

  border: .125rem solid #3b3b3b;
  border-radius: 50%;

  cursor: pointer;
}

svg {
  width: 3.5rem;
  height: 3.5rem;
}

.outer-transcription-container {
  background-color: #2b2b2b;

  font-size: 1.5rem;
  font-family: monospace;
  line-height: 1.5;

  width: 22.5rem;
  max-height: 30rem;

  border: .125rem solid #3b3b3b;
  border-radius: 1.5rem;

  padding: 2rem;
}

.inner-transcription-container {
  width: 100%;
  height: 100%;

  overflow: scroll;
}

.inner-transcription-container::-webkit-scrollbar {
  display: none;
}

.transcription-text-fallback {
  color: #5b5b5b;

  text-align: center;
}
</style>