from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os

from services.summarizer import summarize_text
from services.pdf_handler import extract_text_from_pdf
from services.image_handler import analyze_image
from utils.router import detect_input_type

from fastapi import Request
from fastapi.responses import PlainTextResponse

import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/webhook")
async def whatsapp_webhook(request: Request):

    form = await request.form()

    message_body = form.get("Body")
    num_media = int(form.get("NumMedia", 0))

    if num_media == 0:
        result = summarize_text(message_body)
        reply = result["tldr"]
    else:
        reply = "Media support coming soon."

    return PlainTextResponse(reply)


@app.post("/process/")
async def process(
    file: UploadFile = File(None),
    text: str = Form(None)
):

    input_type = detect_input_type(file, text)

    logging.info(f"Received input type: {input_type}")

    if input_type == "text":
        result = summarize_text(text)

    elif input_type == "pdf":
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = extract_text_from_pdf(file_path)
        result = summarize_text(extracted_text)

    elif input_type == "image":
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = analyze_image(file_path)

    elif input_type == "unsupported_file":
        return {"error": "Unsupported file type"}

    else:
        return {"error": "No input provided"}

    return {
        "input_type": input_type,
        "result": result
    }