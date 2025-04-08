<script setup>
import { ref, onMounted } from "vue";
import { fetchState, fetchResult } from "../utils";
import LoadingSpinner from "../components/LoadingSpinner.vue";
import ErrorModal from "../components/ErrorModal.vue";
import router from "../router";
import store from "../store";

const state = ref(null);

async function poll() {
  state.value = await fetchState(store.taskId);
  if (state.value === "SUCCESS") {
    const [blob, text] = await fetchResult(store.taskId);
    store.transcriptionBlob = blob;
    store.transcriptionText = text;
    router.push("/result");
  } else if (state.value === "STARTED") {
    setTimeout(poll, 500);
  }
}

onMounted(poll);
</script>

<template>
  <div class="wrapper">
    <LoadingSpinner class="loading-spinner" />
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

.loading-spinner {
  width: 4.5rem;
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