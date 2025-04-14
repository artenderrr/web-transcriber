<script setup>
import { useTemplateRef } from "vue";
import { onClickOutside } from "@vueuse/core";
import store from "../store";

const emit = defineEmits(["unfocus"]);
const modalContainer = useTemplateRef("modal-container");

onClickOutside(modalContainer, () => emit("unfocus"));
</script>

<template>
  <div class="modal-wrapper">
    <div class="modal-background"></div>
    <div ref="modal-container" class="modal-container">
      <p>Выберите формат</p>
      <div class="file-formats-container">
        <a :href="store.transcriptionTextUrl" :download="`${Date.now()}.txt`">
          <button @click="$emit('unfocus')">.txt</button>
        </a>
        <a :href="store.transcriptionDocumentUrl" :download="`${Date.now()}.docx`">
          <button @click="$emit('unfocus')">.docx</button>
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-wrapper {
  position: absolute;

  width: 100%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;

  backdrop-filter: blur(10px);
}

.modal-background {
  width: 100%;
  height: 100%;
}

.modal-container {
  position: absolute;

  background-color: #2b2b2b;

  width: 22.5rem;
  height: 12.5rem;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1.5rem;

  border: .125rem solid #3b3b3b;
  border-radius: 1.5rem;
}

.file-formats-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.25rem;
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  background-color: #3b3b3b;
  color: inherit;

  font-size: inherit;
  font-family: monospace;

  width: 8rem;
  height: 3.5rem;

  border: .125rem solid #4b4b4b;
  border-radius: .75rem;

  cursor: pointer;
}
</style>