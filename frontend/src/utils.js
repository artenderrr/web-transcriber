export async function fetchState(taskId) {
  let state;
  try {
    const apiUrl = import.meta.env.VITE_API_URL;
    const response = await fetch(`${apiUrl}/transcriptions/${taskId}/state`);
    const data = await response.json();
    state = data["state"];
  } catch (error) {
    console.error(error);
    state = "FAILURE";
  }
  return state;
}