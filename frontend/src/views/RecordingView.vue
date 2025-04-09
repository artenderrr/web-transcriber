<script setup>
import { ref } from "vue";
import RecordButton from "../components/RecordButton.vue";
import ErrorModal from "../components/ErrorModal.vue";
import store from "../store";
import router from "../router";

const errorContent = ref(null);

function onMicrophoneFailure(cause) {
  if (cause === "unsupported-browser") {
    errorContent.value = "К сожалению, ваш браузер не поддерживает функцию записи звука."
  } else if (cause === "no-microphone-access") {
    errorContent.value = "Не удалось получить доступ к микрофону. Пожалуйста, проверьте разрешения браузера."
  }
}

function onFinishRecording(audioData) {
  store.audioUrl = audioData.audioUrl;
  store.audioDuration = audioData.audioDuration;
  router.push("/player");
}
</script>

<template>
  <div class="wrapper">
    <RecordButton @microphone-failure="onMicrophoneFailure" @finish-recording="onFinishRecording"/>
    <Transition name="fade">
      <ErrorModal v-if="errorContent" header-content="Ой..." :main-content="errorContent" />
    </Transition>
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>