from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.summarize import router as summary_router

app = FastAPI(
    title="Text Summarization API",
    description="API for summarizing text using BERT",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins (e.g., ["http://localhost", "https://yourdomain.com"])
    allow_credentials=True,  # Allow cookies to be sent
    allow_methods=["*"],  # List of allowed HTTP methods (e.g., ["GET", "POST", "PUT"])
    allow_headers=["*"],  # List of allowed headers (e.g., ["Content-Type", "Authorization"])
)

# Include routes
app.include_router(summary_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Summarization API!"}
