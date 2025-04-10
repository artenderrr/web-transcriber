<script setup>
import { ref, useTemplateRef } from "vue";
import RestartButton from "../components/RestartButton.vue";
import AudioPlayer from "../components/AudioPlayer.vue";
import TranscribeButton from "../components/TranscribeButton.vue";
import ErrorModal from "../components/ErrorModal.vue";
import store from "../store";

const audioPlayer = useTemplateRef("audio-player");
const requestFailed = ref(false);

function pauseAudio() {
  audioPlayer.value.audio.pause();
}
</script>

<template>
  <div class="wrapper">
    <RestartButton @restart="pauseAudio"/>
    <AudioPlayer ref="audio-player" :src="store.audioUrl" />
    <TranscribeButton @click="pauseAudio" @request-failure="requestFailed = true" />
    <Transition name="fade">
      <ErrorModal v-if="requestFailed"
      header-content="Ой..."
      main-content="Не получилось отправить запрос на перевод. Пожалуйста, попробуйте ещё раз через какое-то время."
      button-content="Ладно"
      :button-action="() => requestFailed = false" />
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

.wrapper {
  flex-direction: column;
  gap: 1rem;
}
</style>