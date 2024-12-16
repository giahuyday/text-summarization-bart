from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from app.serializers.summary_request import SummaryRequest
from app.services.summarize import TextSummaryService, PdfSummarizer
from io import BytesIO

router = APIRouter(prefix="/summary", tags=["Summarization"])

summary_service = TextSummaryService()

@router.post("/")
async def summarize_text(request: SummaryRequest):
    try:
        result = summary_service.generate_summary(request.text)
        return {"summary": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Khởi tạo đối tượng tóm tắt PDF
pdf_summarizer = PdfSummarizer()

@router.post("/file/")
async def summarize_file(file: UploadFile = File(...)):
    try:
        # Đọc file PDF
        file_content = await file.read()
        
        # Tóm tắt văn bản từ file PDF
        summary = pdf_summarizer.summarize_pdf(BytesIO(file_content))
        
        return JSONResponse(content={"summary": summary})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
