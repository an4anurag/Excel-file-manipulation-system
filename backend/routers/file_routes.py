from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from services import file_service
from utils import file_utils
import os

router = APIRouter()

STORAGE_PATH = "storage/uploaded.xlsx"

# Upload Excel File
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith((".xls", ".xlsx")):
            raise HTTPException(status_code=400, detail="Invalid file format. Only .xls and .xlsx allowed.")
        
        await file_service.save_file(file, STORAGE_PATH)
        
        columns = file_service.get_columns(STORAGE_PATH)
        return {"columns": columns}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


# Perform Operation
@router.post("/operation")
async def perform_operation(request: dict):
    try:
        operation = request.get("operation")
        params = request.get("params")
        
        if not os.path.exists(STORAGE_PATH):
            raise HTTPException(status_code=400, detail="No file uploaded yet.")
        
        updated_columns, preview = file_service.apply_operation(STORAGE_PATH, operation, params)
        return {"columns": updated_columns, "preview": preview}
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Operation failed: {str(e)}")




# Download Updated File
@router.get("/download")
async def download_file():
    try:
        if not os.path.exists(STORAGE_PATH):
            raise HTTPException(status_code=400, detail="No file uploaded yet.")
        
        return FileResponse(
            STORAGE_PATH,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename="updated.xlsx",
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")