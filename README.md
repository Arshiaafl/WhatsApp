# WhatsApp Summarizer API

This project provides a FastAPI-based backend for summarizing text, PDF files, and images using Google Gemini models. It is designed for easy integration with messaging platforms like WhatsApp.

## Features
- Summarize plain text with TL;DR, key points, important numbers, and action items
- Extract and summarize text from PDF files
- Analyze and summarize images (including visible text)
- Returns results in structured JSON format

## Endpoints

### `/process-text/`
- **POST**
- Accepts: `text` (string)
- Returns: JSON summary

### `/process-file/`
- **POST**
- Accepts: `file` (PDF or image)
- Returns: JSON summary

## Usage
1. Clone the repository:
   ```powershell
   git clone https://github.com/Arshiaafl/WhatsApp.git
   cd WhatsApp
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Set up your Google Gemini API key:
   - Create a `.env` file in the project root:
     ```
     API=your_google_gemini_api_key
     ```
   - **Do not share your `.env` file. It is excluded from git.**
4. Run the server:
   ```powershell
   uvicorn main:app --reload
   ```

## Project Structure
```
main.py                # FastAPI app entry point
services/              # Summarizer, PDF, and image handlers
utils/router.py        # Input type detection utility
requirements.txt       # Python dependencies
.env                   # API key (excluded from git)
```

## Supported Models
- Gemini 1.5 Flash (free tier)
- Gemini Pro (free tier)

## License
MIT

## Author
Arshiaafl
