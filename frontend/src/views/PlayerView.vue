<script setup>
import store from "../store";
</script>

<template>
  <div class="wrapper">
    <audio v-if="store.audioUrl" :src="store.audioUrl" controls></audio>
  </div>
</template>