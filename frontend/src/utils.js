import { Document, Packer, Paragraph, TextRun } from "docx";

const apiUrl = import.meta.env.VITE_API_URL;
const docxStyles = {
  fontSize: parseFloat(import.meta.env.VITE_DOCX_FONT_SIZE) || 1,
  lineSpacing: parseFloat(import.meta.env.VITE_DOCX_LINE_SPACING) || 1.15,
  pageMargin: parseFloat(import.meta.env.VITE_DOCX_PAGE_MARGIN) || 1,
};

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

export async function convertTextBlobToDocBlob(blob) {
  const text = await blob.text();

  const fontSize = docxStyles.fontSize * 24;
  const lineSpacing = fontSize * docxStyles.lineSpacing * 10;
  const pageMargin = 1440 * docxStyles.pageMargin;

  const doc = new Document({
    sections: [{
      properties: {
        page: {
          margin: {
            top: pageMargin,
            bottom: pageMargin,
            left: pageMargin,
            right: pageMargin
          }
        }
      },
      children: [
        new Paragraph({
          spacing: {
            line: lineSpacing,
            lineRule: "AUTO"
          },
          children: [
            new TextRun({ text, size: fontSize })
          ]
        })
      ]
    }]
  });
  const docBlob = await Packer.toBlob(doc);
  return docBlob;
}