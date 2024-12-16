from app.models.bert import BertSummarizer
import fitz  # PyMuPDF
from transformers import BartForConditionalGeneration, BartTokenizer

class TextSummaryService:
    def __init__(self):
        self.summarizer = BertSummarizer()

    def generate_summary(self, text: str) -> str:
        return self.summarizer.summarize(text)

class PdfSummarizer:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        # Khởi tạo mô hình BART từ Hugging Face
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)

    def summarize_pdf(self, file_stream):
        """
        Tóm tắt văn bản từ file PDF.
        """
        # Mở file PDF từ BytesIO
        pdf_document = fitz.open(stream=file_stream, filetype="pdf")
        
        # Kết hợp tất cả các trang thành một chuỗi văn bản
        full_text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            full_text += page.get_text()

        # Tóm tắt văn bản
        return self.summarize(full_text)

    def summarize(self, text: str, max_length: int = 130, min_length: int = 30, length_penalty: float = 2.0) -> str:
        """
        Tóm tắt văn bản bằng mô hình BART.
        """
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = self.model.generate(
            inputs,
            max_length=max_length,
            min_length=min_length,
            length_penalty=length_penalty,
            num_beams=4,
            early_stopping=True
        )
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
