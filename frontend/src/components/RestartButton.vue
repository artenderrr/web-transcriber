<script setup>
import router from "../router";
import store from "../store";

const emit = defineEmits(["restart"]);

function onClick() {
  emit("restart");
  URL.revokeObjectURL(store.audioUrl);
  router.push("/");
}
</script>

<template>
  <div class="container" @click="onClick">
    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 12 12"><path fill="currentColor" d="M10.5 2A.75.75 0 0 0 9 2v.646a4.5 4.5 0 1 0 1.42 4.206c.088-.465-.304-.852-.777-.852c-.355 0-.636.291-.711.638a3.001 3.001 0 1 1-1.266-3.133H7.25a.75.75 0 0 0 0 1.5h2.5a.75.75 0 0 0 .75-.75z"/></svg>
  </div>
</template>

<style scoped>
.container {
  background-color: #2b2b2b;
  color: #5b5b5b;

  width: 5rem;
  aspect-ratio: 1 / 1;

  display: flex;
  justify-content: center;
  align-items: center;

  border: .125rem solid #3b3b3b;
  border-radius: 50%;

  cursor: pointer;
}

.container > svg {
  display: block;
}

svg {
  width: 3rem;
  height: 3rem;
}
</style>