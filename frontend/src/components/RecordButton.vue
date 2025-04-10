<script setup>
import { ref, onMounted } from "vue";

const emit = defineEmits(["microphone-failure", "finish-recording"]);

const isRecording = ref(false);

let supportedMimeType;

function defineSupportedMimeType() {
  const types = [
    "audio/webm;codecs=opus",
    "audio/webm",
    "audio/ogg;codecs=opus",
    "audio/ogg",
    "audio/mp4"
  ]

  supportedMimeType = types.find(type => MediaRecorder.isTypeSupported(type));
}

let stream;
let recorder;
let recordingStartedAt;
let audioDuration;

async function onClick() {
  isRecording.value = !isRecording.value;

  if (isRecording.value) {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      console.error("This browser doesn't support audio recording!");
      isRecording.value = false;
      emit("microphone-failure", "unsupported-browser");
      return;
    }

    try {
      stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      recorder = new MediaRecorder(stream, { mimeType: supportedMimeType });

      const audioChunks = [];

      recorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
      }

      recorder.onstop = (event) => {
        const audioBlob = new Blob(audioChunks, { type: supportedMimeType });
        const audioUrl = URL.createObjectURL(audioBlob);
        stream.getTracks().forEach(track => track.stop());
        emit("finish-recording", { audioUrl, audioDuration });
      }

      recorder.start();
      recordingStartedAt = Date.now();

    } catch (error) {
      console.error("Failed to access microphone!", error);
      isRecording.value = false;
      emit("microphone-failure", "no-microphone-access");
    }

  } else {
    recorder.stop();
    audioDuration = (Date.now() - recordingStartedAt) / 1000;
  }
}

onMounted(defineSupportedMimeType);
</script>

<template>
  <button @click="onClick">
    <div class="circle">
      <div class="circle" :class="{ pulsing: isRecording }"></div>
    </div>
    <span>{{ !isRecording ? "Начать запись" : "Закончить запись" }}</span>
  </button>
</template>

<style scoped>
button {
  background-color: #2b2b2b;
  color: #cdcdcd;

  font: inherit;

  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.25rem;

  border: .125rem solid #3b3b3b;
  border-radius: 1.5rem;

  padding: 1rem;
  padding-inline: 1.5rem;

  cursor: pointer;
}

.circle {
  background-color: #c9184a;

  width: 1.5rem;
  aspect-ratio: 1 / 1;

  border-radius: 50%;
}

.pulsing {
  animation: pulse 1s ease infinite;
}

@keyframes pulse {
  to {
    transform: scale(1.75);
    opacity: 0;
  }
}
</style>