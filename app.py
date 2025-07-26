import os
import io
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load env vars
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

# Cache the uploaded file
uploaded_file_ref = None

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global uploaded_file_ref
    file = request.files["pdf"]
    pdf_data = io.BytesIO(file.read())
    uploaded_file_ref = genai.upload_file(pdf_data, mime_type="application/pdf")
    return jsonify({"status": "uploaded", "file_uri": uploaded_file_ref.uri})

@app.route("/ask", methods=["POST"])
def ask():
    global uploaded_file_ref
    if uploaded_file_ref is None:
        return jsonify({"error": "No PDF uploaded yet"}), 400

    data = request.get_json()
    question = data.get("question")

    prompt = [
        "You are a precise assistant answering questions based only on the PDF content.",
        "Answer each question in one line. No extra commentary.",
        "Examples:",
        "User Question: অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?",
        "Expected Answer: শুম্ভুনাথ",
        "User Question: কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?",
        "Expected Answer: মামাকে",
        "Now answer:",
        f"User Question: {question}",
        uploaded_file_ref
    ]

    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
