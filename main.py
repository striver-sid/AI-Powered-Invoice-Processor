from fastapi import FastAPI
import uvicorn
from code.routes.invoice import router

app=FastAPI(title="AI Powered Invoice Processor")
app.include_router(router,prefix="/erp",tags=["invoices"])

if __name__=="__main__":  
    uvicorn.run(app,host="127.0.0.1",port=8000)

