import { createRouter, createMemoryHistory } from "vue-router";

import RecordingView from "./views/RecordingView.vue";
import PlayerView from "./views/PlayerView.vue";
import PendingView from "./views/PendingView.vue";
import TranscriptionView from "./views/TranscriptionView.vue";
import ResultView from "./views/ResultView.vue";
import PreviewView from "./views/PreviewView.vue";

const routes = [
  { path: "/", component: RecordingView },
  { path: "/player", component: PlayerView },
  { path: "/pending", component: PendingView },
  { path: "/transcription", component: TranscriptionView },
  { path: "/result", component: ResultView },
  { path: "/preview", component: PreviewView }
];

const router = createRouter({
  routes,
  history: createMemoryHistory()
});

export default router;