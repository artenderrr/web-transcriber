<script setup>
import { useTemplateRef } from "vue";
import { onClickOutside } from "@vueuse/core";

const emit = defineEmits(["unfocus"]);
const modalContainer = useTemplateRef("modal-container");

onClickOutside(modalContainer, () => emit("unfocus"));
</script>

<template>
  <div class="modal-wrapper">
    <div class="modal-background"></div>
    <div ref="modal-container" class="modal-container"></div>
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

  border: .125rem solid #3b3b3b;
  border-radius: 1.5rem;
}
</style>