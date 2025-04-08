<script setup>
import { computed } from "vue";
const props = defineProps(["header-content", "main-content", "button-content", "button-action"]);

const headerContent = computed(() => props.headerContent || "Ошибка");
const mainContent = computed(() => props.mainContent || "Что-то пошло не так.");
</script>

<template>
  <div class="error-modal-wrapper">
    <div class="error-modal-container">
      <p class="error-modal-header">{{ headerContent }}</p>
      <p class="error-modal-main-content">{{ mainContent }}</p>
      <button v-if="props.buttonContent" @click="props.buttonAction">
        {{ props.buttonContent }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.error-modal-wrapper {
  position: absolute;

  background-color: #1b1b1b;

  width: 100%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}

.error-modal-container {
  background-color: #800f2f;
  color: #ff8fa3;

  width: 22.5rem;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: .5rem;

  border: .125rem solid #a4133c;
  border-radius: 1.5rem;

  padding: 1.5rem;

  transition: transform .5s;
}

.error-modal-header {
  font-size: 3rem;
  font-weight: bold;
}

.error-modal-main-content {
  font-size: 1.5rem;
  text-align: center;
  line-height: 1.5;
}

button {
  background-color: #a4133c;
  color: #ffb3c1;

  font: inherit;

  border: none;
  border-radius: .75rem;

  padding: .5rem;
  padding-inline: 1.25rem;

  margin-top: .5rem;

  cursor: pointer;
}
</style>