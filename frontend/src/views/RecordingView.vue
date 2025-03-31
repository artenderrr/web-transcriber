<script setup>
import RecordButton from "../components/RecordButton.vue";
import store from "../store";
import router from "../router";

function onFinishRecording(newAudioUrl) {
  store.audioUrl = newAudioUrl;
  router.push("/player");
}
</script>

<template>
  <div class="wrapper">
    <RecordButton @finish-recording="onFinishRecording"/>
  </div>
</template>