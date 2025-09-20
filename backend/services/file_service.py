import pandas as pd
from fastapi import UploadFile, HTTPException
import shutil

# Save uploaded file
async def save_file(file: UploadFile, path: str):
    try:
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")


# Get column names from Excel
def get_columns(path: str):
    try:
        df = pd.read_excel(path)
        return list(df.columns)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading columns: {str(e)}")


# Apply operation
def apply_operation(path: str, operation: str, params: dict):
    try:
        df = pd.read_excel(path)
        
        if operation == "add_column":
            new_col = params["new_column_name"]
            cols = params["columns_to_sum"]
            
            if len(cols) != 2:
                raise HTTPException(status_code=400, detail="Exactly 2 columns required for add_column.")
            df[new_col] = df[cols[0]] + df[cols[1]]
            
        elif operation == "combine_two_columns":
            new_col = params.get("new_column_name", "Combined")
            cols = params["columns"]

            if len(cols) != 2:
                raise HTTPException(status_code=400, detail="Exactly 2 columns required for combine_two_columns.")
            df[new_col] = df[cols[0]] + df[cols[1]]
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported operation: {operation}")
        
        df.to_excel(path, index=False)
        
        return list(df.columns), df.head(5).to_dict(orient="records")
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error applying operation: {str(e)}")