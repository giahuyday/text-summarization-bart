# Summarizer Project

This project provides a FastAPI-based API to upload a PDF file and summarize its content using a text summarization model (e.g., BART).

---

## **Features**

-   **File Upload API**: Accepts PDF files from the frontend.
-   **PDF Parsing**: Extracts text from the uploaded PDF file.
-   **Text Summarization**: Summarizes the extracted text using the BART model from Hugging Face.
-   **Response in JSON**: Returns the summarized text in JSON format.

---

## **Requirements**

-   Python 3.8+

### **Dependencies**

Install the required libraries by running:

```bash
pip install -r requirements.txt
```

**Key Libraries:**

-   `fastapi`: Framework to build APIs.
-   `uvicorn`: ASGI server to run FastAPI.
-   `transformers`: Hugging Face library for pre-trained NLP models.
-   `torch`: Deep learning framework required by transformers.
-   `PyMuPDF`: Library to extract text from PDF files.

---

## **Project Structure**

```
└── 📁seminar_ke
    └── 📁app
        └── 📁models
            └── bert.py
        └── 📁routes
            └── summarize.py
        └── 📁schemasmas
            └── summary_request.py
        └── 📁services
            └── summarize.py
        └── __init__.py
        └── config.py
        └── main.py
    └── README.md
    └── requirements.txt
```

---

## **Running the Project**

### 1. Clone the Repository

```bash
git clone git@github.com:giahuyday/text-summarization-bart.git
cd text-summarization-bart
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000/`.

---

## **Using the API**

### **Endpoint**: `POST /summary/file`

-   **Description**: Accepts a PDF file and returns a summarized version of its text.
-   **Request Format**: Multipart form-data
-   **Response Format**: JSON

### Example Request with `curl`

```bash
curl -X 'POST' 'http://127.0.0.1:8000/summary/file' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@path_to_your_pdf_file.pdf'
```

### **Endpoint**: `POST /summary/`

-   **Description**: Accepts a text and returns a summarized version of its text.
-   **Response Format**: JSON

### Example Request with `curl`

```bash
curl -X 'POST' 'http://127.0.0.1:8000/summary/' -H 'accept: application/json' -F 'file=@path_to_your_pdf_file.pdf'
```
