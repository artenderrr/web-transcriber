import { reactive } from "vue";

const store = reactive({
  audioUrl: null,
  audioDuration: null,
  taskId: null,
  transcriptionTextUrl: null,
  transcriptionDocumentUrl: null,
  transcriptionPDFUrl: null,
  transcriptionText: null
});

function resetStore() {
  for (const key in store) {
    store[key] = null;
  }
}

function revokeUrls() {
  URL.revokeObjectURL(store.audioUrl);
  URL.revokeObjectURL(store.transcriptionTextUrl);
  URL.revokeObjectURL(store.transcriptionDocumentUrl);
  URL.revokeObjectURL(store.transcriptionPDFUrl);
}

export function clearStore() {
  revokeUrls();
  resetStore();
}

export default store;