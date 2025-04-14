<script setup>
import { ref } from "vue";
import RestartButton from "../components/RestartButton.vue";
import FileSelectionModal from "../components/FileSelectionModal.vue";
import router from "../router";
import store from "../store";

const fileSelection = ref(false);
const transcriptionFileName = ref(`${Date.now()}.txt`);

function openPreview() {
  router.push("/preview");
}
</script>

<template>
  <div class="wrapper">
    <RestartButton class="restart-button" />
    <p class="result-message">Готово!</p>
    <button @click="fileSelection = true">
      <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24"><g fill="none"><path d="m12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035q-.016-.005-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093q.019.005.029-.008l.004-.014l-.034-.614q-.005-.018-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z"/><path fill="currentColor" d="M12 2v6.5a1.5 1.5 0 0 0 1.356 1.493L13.5 10H20v10a2 2 0 0 1-1.85 1.995L18 22H6a2 2 0 0 1-1.995-1.85L4 20V4a2 2 0 0 1 1.85-1.995L6 2zm2 .043a2 2 0 0 1 .877.43l.123.113L19.414 7a2 2 0 0 1 .502.84l.04.16H14z"/></g></svg>
      <div class="button-text-container">
        <span>Скачать файл</span>
      </div>
    </button>
    <p class="separator">или</p>
    <button @click="openPreview">
      <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24"><path fill="currentColor" d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5M12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5s5 2.24 5 5s-2.24 5-5 5m0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3s3-1.34 3-3s-1.34-3-3-3"/></svg>
      <div class="button-text-container">
        <span>Открыть</span>
        <span>предосмотр</span>
      </div>
    </button>
    <Transition name="fade">
      <FileSelectionModal v-if="fileSelection" @unfocus="fileSelection = false" />
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

.result-message {
  color: #3b3b3b;

  font-size: 3rem;
  font-weight: bold;

  margin-bottom: .25rem;
}

button {
  background-color: #2b2b2b;
  color: inherit;

  font: inherit;

  width: 20rem;
  height: 7rem;

  display: flex;
  justify-content: space-evenly;
  align-items: center;

  border: .125rem solid #3b3b3b;
  border-radius: 1.5rem;

  cursor: pointer;
}

.separator {
  color: #3b3b3b;
  line-height: .75;

  margin-bottom: .3rem;
}

svg {
  width: 3.5rem;
  height: 3.5rem;

  color: #5b5b5b;
}

.button-text-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>