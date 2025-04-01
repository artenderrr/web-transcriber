<script setup>
import RecordButton from "../components/RecordButton.vue";
import store from "../store";
import router from "../router";

function onFinishRecording(audioData) {
  store.audioUrl = audioData.audioUrl;
  store.audioDuration = audioData.audioDuration;
  router.push("/player");
}
</script>

<template>
  <div class="wrapper">
    <RecordButton @finish-recording="onFinishRecording"/>
  </div>
</template>