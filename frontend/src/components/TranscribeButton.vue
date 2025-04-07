<script setup>
import { ref } from "vue";
import LoadingSpinner from "./LoadingSpinner.vue";
import router from "../router";
import store from "../store";

const isLoading = ref(false);

async function getAudioFormData(audioUrl) {
  const blob = await (await fetch(audioUrl)).blob();
  const ext = blob.type.split("/")[1];
  const filename = `${Date.now()}.${ext}`

  const formData = new FormData();
  formData.append("audio", blob, filename);

  return formData;
}

async function requestTranscription(formData) {
  const apiUrl = import.meta.env.VITE_API_URL;
  const response = await fetch(`${apiUrl}/transcriptions`, {
    method: "POST",
    body: formData
  });
  const data = await response.json();
  const taskId = data["task_id"];

  return taskId;
}

async function onClick() {
  if (!isLoading.value) {
    isLoading.value = true;

    const formData = await getAudioFormData(store.audioUrl);
    const taskId = await requestTranscription(formData);
    store.taskId = taskId;

    isLoading.value = false;

    router.push("/pending");
  }
}
</script>

<template>
  <div class="transcribe-button-container" @click="onClick">
    <Transition name="fade" mode="out-in">
      <div v-if="!isLoading" class="transcribe-button-content-wrapper">
        <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M9 4.5a.75.75 0 0 1 .721.544l.813 2.846a3.75 3.75 0 0 0 2.576 2.576l2.846.813a.75.75 0 0 1 0 1.442l-2.846.813a3.75 3.75 0 0 0-2.576 2.576l-.813 2.846a.75.75 0 0 1-1.442 0l-.813-2.846a3.75 3.75 0 0 0-2.576-2.576l-2.846-.813a.75.75 0 0 1 0-1.442l2.846-.813A3.75 3.75 0 0 0 7.466 7.89l.813-2.846A.75.75 0 0 1 9 4.5m9-3a.75.75 0 0 1 .728.568l.258 1.036a2.63 2.63 0 0 0 1.91 1.91l1.036.258a.75.75 0 0 1 0 1.456l-1.036.258a2.63 2.63 0 0 0-1.91 1.91l-.258 1.036a.75.75 0 0 1-1.456 0l-.258-1.036a2.63 2.63 0 0 0-1.91-1.91l-1.036-.258a.75.75 0 0 1 0-1.456l1.036-.258a2.63 2.63 0 0 0 1.91-1.91l.258-1.036A.75.75 0 0 1 18 1.5M16.5 15a.75.75 0 0 1 .712.513l.394 1.183c.15.447.5.799.948.948l1.183.395a.75.75 0 0 1 0 1.422l-1.183.395a1.5 1.5 0 0 0-.948.948l-.395 1.183a.75.75 0 0 1-1.422 0l-.395-1.183a1.5 1.5 0 0 0-.948-.948l-1.183-.395a.75.75 0 0 1 0-1.422l1.183-.395a1.5 1.5 0 0 0 .948-.948l.395-1.183A.75.75 0 0 1 16.5 15" clip-rule="evenodd"/></svg>
        <div class="transcription-text-container">
          <span>Перевести</span>
          <span>в текст</span>
        </div>
      </div>
      <div v-else class="transcribe-button-content-wrapper">
        <LoadingSpinner />
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .25s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.transcribe-button-container {
  background-color: #2b2b2b;

  width: 20rem;
  height: 7.5rem;

  border: .125rem solid #3b3b3b;
  border-radius: 1.5rem;

  cursor: pointer;
}

.transcribe-button-content-wrapper {
  height: 100%;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.75rem;
}

.transcription-text-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

svg {
  color: #7b7b7b;

  width: 3.5rem;
  height: 3.5rem;
}
</style>