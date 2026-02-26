from fastapi import UploadFile

def detect_input_type(file: UploadFile | None, text: str | None):

    if file:
        content_type = file.content_type or ""

        if content_type == "application/pdf" or file.filename.lower().endswith(".pdf"):
            return "pdf"

        elif content_type.startswith("image/"):
            return "image"

        else:
            return "unsupported_file"

    elif text:
        return "text"

    return "empty"