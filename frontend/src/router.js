import { createRouter, createWebHistory } from "vue-router";

import RecordingView from "./views/RecordingView.vue";

const routes = [
  { path: "/", component: RecordingView }
];

const router = createRouter({
  routes,
  history: createWebHistory()
});

export default router;