import html2pdf from "html2pdf.js";
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

function splitIntoLines({ text, font, size, maxLineWidth }) {
  const rmSize = 16;
  [size, maxLineWidth] = [size * rmSize, maxLineWidth * rmSize];

  const canvas = document.createElement("canvas");
  const ctx = canvas.getContext("2d");
  ctx.font = `${size}px ${font}`;

  const words = text.split(" ");
  const lines = [];
  let line = [];
  for (const word of words) {
    const lineString = line.concat([word]).join(" ");
    const lineWidth = ctx.measureText(lineString).width;
    if (lineWidth <= maxLineWidth) {
      line.push(word);
    } else {
      lines.push(line.join(" "));
      line = [word];
    }
  }
  if (line.length) lines.push(line.join(" "));

  return lines;
}

function splitIntoPages({ lines, linesPerPage }) {
  const pages = [];
  let page = [];

  for (let line of lines) {
    page.push(line);
    if (page.length === linesPerPage) {
      pages.push(page);
      page = [];
    }
  }
  if (page.length) pages.push(page);

  return pages;
}

export async function convertTextToPDFBlob(text) {
  const [font, size, maxLineWidth] = ["Times New Roman", 1.5, 42.5];

  const lines = splitIntoLines({ text, font, size, maxLineWidth });
  const pages = splitIntoPages({ lines, linesPerPage: 21 });

  const pageElements = pages.reduce((res, page) => {
    const paragraphs = page.reduce((res, line) => {
      return res.concat([`<p>${line}</p>`]);
    }, []).join("");
    return res.concat(
      [`<div class="page"><div style="width: ${maxLineWidth}rem;">${paragraphs}</div></div>`]
    );
  }, []).join("");

  const html = `
  <style>
    * {
      padding: 0;
      margin: 0;
      box-sizing: border-box;
    }

    .page {
      width: 210mm;
      height: 297mm;

      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: center;

      padding-top: 3.425rem;
    }

    p {
      color: black;
      font-family: ${font};
      font-size: ${size}rem;
      line-height: 2;
      break-inside: avoid;
    }
  </style>

  ${pageElements}`;

  const PDFBlob = await html2pdf().from(html).output("blob");
  return PDFBlob;
}