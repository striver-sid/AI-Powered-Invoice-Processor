from fastapi import APIRouter #package for route
router=APIRouter()

@router.get("/process-invoice")
async def processInvoice():
    return {"message":"Invoice processed"}


