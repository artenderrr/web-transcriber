<script setup>
import PlaybackBar from "./PlaybackBar.vue";
import PlaybackControls from "./PlaybackControls.vue";

defineProps(["src"]);
</script>

<template>
  <div class="container">
    <PlaybackBar :progress="20" />
    <PlaybackControls />
  </div>
</template>

<style scoped>
.container {
  background-color: #2b2b2b;
  
  width: 20rem;
  height: 12rem;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  border: .125rem solid #3b3b3b;
  border-radius: 1.5rem;

  padding: 1rem;
}
</style>