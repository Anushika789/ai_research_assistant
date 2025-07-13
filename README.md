AI Research Assistant:
A modular, user-friendly Streamlit web application for document analysis, summarization, semantic search, question answering, and logic challenge generation.
Built with Python, Hugging Face Transformers, Sentence Transformers, pandas, NumPy, and pytesseract for robust data and document processing.

Features:
Document Upload: Supports PDF, DOCX, TXT, and image files.

Automatic Summarization: Generates concise summaries using advanced NLP models.

Semantic Search: Retrieves the most relevant passages from your documents.

Question Answering: Answers user questions based on uploaded content.

Challenge Mode: Generates logic and comprehension questions for study or practice.

OCR: Extracts text from images using pytesseract.

Installation
Clone the repository:

text
git clone https://github.com/Anushika789/ai_research_assistant.git
cd ai_research_assistant
Set up a virtual environment:

text
python -m venv .venv
Activate the virtual environment:

Windows (PowerShell):

text
.venv\Scripts\Activate.ps1
Windows (Cmd):

text
.venv\Scripts\activate.bat
macOS/Linux:

text
source .venv/bin/activate
Install dependencies:

text
pip install -r requirements.txt
Usage
Start the Streamlit app:

text
streamlit run app.py
Open your browser to the link shown in the terminal (usually http://localhost:8501).

Project Structure
text
ai_research_assistant/
├── app.py
├── requirements.txt
├── modules/
│   ├── summarizer.py
│   ├── retriever.py
│   ├── qa.py
│   └── challenge.py
├── assets/
│   └── logo.png
└── README.md

Dependencies:
streamlit
transformers
sentence-transformers
pandas
numpy
pytesseract
pdfplumber
python-docx
(See requirements.txt for the full list.)

Notes:
The first run may take longer as models are downloaded.
All processing is local; your documents are not uploaded to any server.
For best performance, use a machine with adequate RAM and a stable internet connection.
