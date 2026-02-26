import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API")
if not key:
    raise RuntimeError("Google API key not found. Set API in .env.")
genai.configure(api_key=key)

model = genai.GenerativeModel('gemini-2.5-flash')

def analyze_image(image_path: str):
    image = Image.open(image_path)
    # Convert image to bytes for Gemini API
    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()
    response = model.generate_content([
        image_bytes,
        "Describe this image. Extract visible text. Summarize its meaning. "
    ])
    return response.text




