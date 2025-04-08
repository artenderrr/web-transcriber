<script setup>
import store from "../store";
</script>

<template>
  <div class="wrapper">
    <p>{{ store.transcriptionText }}</p>
  </div>
</template>

<style scoped>
.wrapper {
  flex-direction: column;
}
</style>