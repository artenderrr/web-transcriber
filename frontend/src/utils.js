const apiUrl = import.meta.env.VITE_API_URL;

export async function fetchState(taskId) {
  let state;
  try {
    const response = await fetch(`${apiUrl}/transcriptions/${taskId}/state`);
    const data = await response.json();
    state = data["state"];
  } catch (error) {
    console.error(error);
    state = "FAILURE";
  }
  return state;
}

export async function fetchResult(taskId) {
  let blob, text;
  try {
    const response = await fetch(`${apiUrl}/transcriptions/${taskId}`);
    blob = await response.blob();
    text = await blob.text();
  } catch (error) {
    console.error(error);
    [blob, text] = [null, null];
  }
  return [blob, text];
}