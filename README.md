# Web-Based PDF Text Extractor

This project provides a simple web application to extract text from PDF files. It consists of a Python backend (using Flask) and a frontend built with HTML, CSS, and JavaScript.

## 1. Getting Started

Follow these steps to set up and run the PDF Text Extractor on your local machine.

### Prerequisites

You need to have **Python 3.x** installed on your system.

### Installation

1.  **Navigate to your project folder:**
    Open your terminal or command prompt and go to the `Pdf extractor` folder where you have `pdf_extractor.py` (your backend file) and `index.html`.
    ```bash
    cd "C:\Users\Nouman Khan\Desktop\Pdf extractor"
    ```
    *(Replace `C:\Users\Nouman Khan\Desktop\Pdf extractor` with the actual path to your project folder if it's different.)*

2.  **Install Python Libraries:**
    You need to install the following Python libraries: `Flask`, `PyPDF2`, and `Flask-Cors`.
    Run this command in your terminal:
    ```bash
    pip install Flask PyPDF2 Flask-Cors
    ```

## 2. Project Structure

Your project folder should look like this:

```
Pdf extractor/
├── pdf_extractor.py
└── index.html
```

*   **`pdf_extractor.py`**: This is your main Python backend file. It contains the Flask web server setup and the logic for *actually extracting text from PDFs*. You will run this file to start the server.
*   **`index.html`**: This is the web page (frontend) you open in your browser. It allows you to select a PDF and sends it to your `pdf_extractor.py` backend for processing.

## 3. Usage

To use the application:

1.  **Start the Backend Server:**
    In your terminal (still in the `Pdf extractor` folder), run your Flask application:
    ```bash
    python pdf_extractor.py
    ```
    Keep this terminal window open. You should see a message indicating the server is running, usually on `http://127.0.0.1:5000`.

2.  **Open the Frontend:**
    Locate the `index.html` file in your `Pdf extractor` folder and double-click it to open it in your web browser.

3.  **Extract Text:**
    *   Click the "Choose File" button on the web page.
    *   Select a PDF document from your computer.
    *   Click the "Extract Text" button.
    *   The extracted text from your PDF will appear in the text area on the page.
