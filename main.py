from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI(title="AI-Powered Invoice Processor", description="A simple API to process invoices using AI")

@app.post("/process-invoice/")
async def process_invoice(file: UploadFile = File(...)):
    # Save the uploaded file temporarily
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Here you would integrate with AI model to process the invoice
    # For now, just return a mock response
    result = {
        "filename": file.filename,
        "status": "processed",
        "extracted_data": {
            "total_amount": 123.45,
            "date": "2023-10-01",
            "vendor": "Example Vendor"
        }
    }

    # Clean up temp file
    os.remove(file_path)

    return JSONResponse(content=result)

@app.get("/")
async def root():
    return {"message": " Invoice Processor API "}
#this is the main file
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)