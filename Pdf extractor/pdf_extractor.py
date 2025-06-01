# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS # Used to handle Cross-Origin Resource Sharing
import PyPDF2
import io
import os

app = Flask(__name__)
# Enable CORS for all routes, allowing your frontend (even if opened via file://)
# to make requests to this Flask backend. In production, you'd specify origins.
CORS(app) 

# Function to extract text from a PDF file stream
# This is modified to work with file-like objects received via HTTP POST
def extract_text_from_pdf_stream(pdf_file_stream):
    """
    Extracts all text from a PDF file stream (e.g., from an uploaded file).

    Args:
        pdf_file_stream: A file-like object (e.g., werkzeug.datastructures.FileStorage from request.files).

    Returns:
        str: The extracted text, or an error message.
    """
    try:
        # Use io.BytesIO to ensure PyPDF2 can read from the stream
        pdf_reader = PyPDF2.PdfReader(pdf_file_stream)
        
        if pdf_reader.is_encrypted:
            # You might attempt to decrypt here if you have a known password
            # e.g., pdf_reader.decrypt('your_password')
            return "Error: The PDF file is encrypted and cannot be processed.", 400

        extracted_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"

        if not extracted_text.strip():
            return "Warning: No readable text found in the PDF. It might be an image-only document.", 200

        return extracted_text.strip(), 200 # Return text and HTTP 200 OK
    except PyPDF2.errors.PdfReadError:
        return "Error: Could not read the PDF file. It might be corrupted or not a valid PDF.", 400
    except Exception as e:
        return f"An unexpected error occurred: {e}", 500

@app.route('/extract_pdf', methods=['POST'])
def handle_extract_pdf():
    """
    API endpoint to receive a PDF file and return its extracted text.
    """
    if 'pdf_file' not in request.files:
        return jsonify({"error": "No PDF file provided"}), 400

    pdf_file = request.files['pdf_file']
    
    # Check if the file is empty
    if pdf_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Check file type
    if not pdf_file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Invalid file type. Please upload a PDF."}), 400

    # Extract text from the uploaded file stream
    extracted_text, status_code = extract_text_from_pdf_stream(pdf_file.stream)

    if status_code != 200:
        return jsonify({"error": extracted_text}), status_code
    
    return jsonify({"extracted_text": extracted_text}), status_code

@app.route('/')
def home():
    return "PDF Extractor Backend is running. Access the frontend via index.html."

if __name__ == '__main__':
    # You can change the port if 5000 is in use, e.g., app.run(port=5001)
    app.run(debug=True, port=5000) # debug=True allows auto-reloading and helpful error messages
