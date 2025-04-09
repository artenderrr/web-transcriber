import { reactive } from "vue";

const store = reactive({
  audioUrl: null,
  audioDuration: null,
  taskId: null,
  transcriptionUrl: null,
  transcriptionText: null
});

function resetStore() {
  for (const key in store) {
    store[key] = null;
  }
}

function revokeUrls() {
  URL.revokeObjectURL(store.audioUrl);
  URL.revokeObjectURL(store.transcriptionUrl);
}

export function clearStore() {
  revokeUrls();
  resetStore();
}

export default store;