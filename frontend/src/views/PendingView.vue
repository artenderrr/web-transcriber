<script setup>
import store from "../store";

console.log(`[LOG] taskId: ${store.taskId}`);
</script>

<template>
  <div class="wrapper">
    <p>Waiting in queue...</p>
  </div>
</template>