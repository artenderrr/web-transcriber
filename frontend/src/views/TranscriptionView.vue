<script setup>
import { ref, onMounted } from "vue";
import { fetchState, fetchResult } from "../utils";
import { convertTextBlobToDocBlob, convertTextToPDFBlob } from "../utils";
import ProgressNumber from "../components/ProgressNumber.vue";
import ProgressBar from "../components/ProgressBar.vue";
import ErrorModal from "../components/ErrorModal.vue";
import router from "../router";
import store from "../store";

const state = ref("STARTED");
const progress = ref(0);

async function poll() {
  state.value = await fetchState(store.taskId);
  if (state.value === "SUCCESS") {
    progress.value = 100;
    const [blob, text] = await fetchResult(store.taskId);
    store.transcriptionTextUrl = URL.createObjectURL(blob);
    store.transcriptionDocumentUrl = URL.createObjectURL(
      await convertTextBlobToDocBlob(blob)
    );
    store.transcriptionPDFUrl = URL.createObjectURL(
      await convertTextToPDFBlob(text)
    );
    store.transcriptionText = text;
    router.push("/result");
  } else if (state.value === "STARTED") {
    setTimeout(poll, 500);
  }
}

function updateProgress() {
  const audioDurationInMs = store.audioDuration * 1000;
  if (state.value === "STARTED") {
    progress.value += 1;
    if (progress.value < 90) {
      const fourtyPercentOfAudioDuration = audioDurationInMs / 100 * 40;
      const percentsPerSecond = 90 / fourtyPercentOfAudioDuration * 1000;
      const updateSpeed = 1000 / percentsPerSecond;
      setTimeout(updateProgress, updateSpeed);
    } else if (progress.value >= 90 && progress.value < 99) {
      const updateSpeed = audioDurationInMs / 100 * 10;
      setTimeout(updateProgress, updateSpeed);
    }
  }
}

onMounted(() => {
  poll();
  updateProgress();
})
</script>

<template>
  <div class="wrapper">
    <ProgressNumber v-bind="{ progress }" />
    <ProgressBar v-bind="{ progress }" />
    <div class="transcription-text-container">
      <span class="upper-text">Переводим в текст.</span>
      <span>Пожалуйста, подождите...</span>
    </div>
    <Transition name="fade">
      <ErrorModal v-if="state === 'FAILURE'"
      header-content="Ой..."
      main-content="Что-то пошло не так. Пожалуйста, попробуйте ещё раз."
      button-content="Ладно"
      :button-action="() => router.go(-2)" />
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
  gap: 1.25rem;

  color: #5b5b5b;
}

.transcription-text-container {
  font-size: 1.75rem;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.upper-text {
  color: #424242;
}
</style>