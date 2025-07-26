# Gemini-PDF-QA-Web-App

⚙️ Setup Guide
🔐 1. Clone & Configure Environment

git clone https://github.com/yourusername/gemini-pdf-qa.git
cd gemini-pdf-qa

Create a .env file and add your Gemini API key:

GEMINI_API_KEY=your-api-key-here

🛠 2. Install Dependencies

pip install -r requirements.txt

▶️ 3. Run the App

python app.py

📊 Evaluation Q&A
🧠 1. What method or library did you use to extract the text, and why? Did you face any formatting challenges with the PDF content?

We did not manually extract or chunk the text. Instead, we uploaded the raw PDF directly to Gemini’s file system using genai.upload_file(), allowing the Gemini model to internally process and parse the content. This bypasses traditional Bangla PDF parsing issues, such as broken Unicode rendering, inconsistent spacing, and font misalignment — common challenges with libraries like PyPDF2 or PyPDFLoader. Gemini's internal handling eliminates these formatting concerns, making it highly efficient for question-answering tasks on Bangla documents.


✂️ 2. What chunking strategy did you choose?

No manual chunking was needed. Gemini’s internal system uses its own context mapping from the uploaded document. This allows seamless and contextually accurate question-answering without having to split the document into sections, paragraphs, or token-limited chunks.


📐 3. What embedding model did you use?

We did not use a traditional embedding model. Instead of relying on vector embeddings or sentence transformers, we leveraged Gemini 2.0 Flash’s native support for file context referencing. This eliminates the need for generating and comparing vector embeddings, which are often unreliable for Bangla content due to limitations in multilingual models.


🧮 4. How are you comparing the query with your stored chunks?

There is no chunk retrieval or similarity scoring involved. The Gemini model accesses the uploaded document file directly and uses its contextual understanding to generate answers. This avoids the need for traditional similarity search methods like cosine similarity or vector databases (e.g., FAISS).


🤖 5. How do you ensure meaningful question-document matching?

We rely on Gemini’s context caching and document understanding capabilities. Since Bangla text extraction from PDFs is often unreliable using standard parsers, Gemini's internal system provides a superior alternative. The model accesses the full content of the uploaded file, and its multimodal architecture enables precise interpretation of questions, even in Bangla. By bypassing manual parsing and embeddings, we ensure that the model always has access to accurate document context when generating responses.

The model is prompted with a consistent template that:

    Instructs the model to be concise

    Gives few-shot examples

    Explicitly attaches the uploaded file as source context

This ensures that even vague or incomplete queries are interpreted in relation to the document.
✅ 6. Are the results relevant?

Yes, most answers are highly relevant due to:

    Zero-shot & few-shot prompting

    Gemini's multimodal PDF understanding

    Explicit instruction on answer formatting

Improvements could include:

    Richer prompt tuning

    Section tagging (e.g., chapter headers)

    Uploading multiple files for context comparison
