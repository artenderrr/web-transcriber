import { createRouter, createMemoryHistory } from "vue-router";

import RecordingView from "./views/RecordingView.vue";
import PlayerView from "./views/PlayerView.vue";
import PendingView from "./views/PendingView.vue";

const routes = [
  { path: "/", component: RecordingView },
  { path: "/player", component: PlayerView },
  { path: "/pending", component: PendingView }
];

const router = createRouter({
  routes,
  history: createMemoryHistory()
});

export default router;