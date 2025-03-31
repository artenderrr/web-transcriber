<script setup>
import { ref } from "vue";
import RecordButton from "../components/RecordButton.vue";

const audioUrl = ref(null);
</script>

<template>
  <div class="wrapper flex-column">
    <RecordButton @finish-recording="newAudioUrl => audioUrl = newAudioUrl"/>
    <audio v-if="audioUrl" :src="audioUrl" controls></audio>
  </div>
</template>

<style scoped>
.flex-column {
  flex-direction: column;
  gap: 1rem;
}
</style>