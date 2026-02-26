import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()
# Configure with your API key
Key = os.getenv("API")
genai.configure(api_key=Key)

# Use the free-tier model (Gemini 1.5 Flash is fast and efficient)
model = genai.GenerativeModel('gemini-2.5-flash')
def summarize_text(text: str):
    prompt = f"""
    Analyze the following content.

    Return STRICTLY in this JSON format (no explanation, no markdown, no text outside the JSON):
    {{
      "tldr": "short summary max 3 lines",
      "key_points": ["point1", "point2"],
      "important_numbers": ["number or date if any"],
      "action_items": ["action if any"]
    }}
    Content:
    {text}
    """
    # Generate text
    response = model.generate_content(prompt)
    try:
        return json.loads(response.text)
    except Exception:
        return response.text