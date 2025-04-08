import { createRouter, createMemoryHistory } from "vue-router";

import RecordingView from "./views/RecordingView.vue";
import PlayerView from "./views/PlayerView.vue";
import PendingView from "./views/PendingView.vue";
import TranscriptionView from "./views/TranscriptionView.vue";

const routes = [
  { path: "/", component: RecordingView },
  { path: "/player", component: PlayerView },
  { path: "/pending", component: PendingView },
  { path: "/transcription", component: TranscriptionView }
];

const router = createRouter({
  routes,
  history: createMemoryHistory()
});

export default router;