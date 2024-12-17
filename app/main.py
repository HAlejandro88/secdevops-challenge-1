from fastapi import FastAPI, File, UploadFile, HTTPException
from app.services.upload_service import scan_file_with_virustotal
from app.config import settings
import os

app = FastAPI()

os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido")
    
    file_location = os.path.join(settings.UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    response = await scan_file_with_virustotal(file_location, file.filename)


    if response.status_code == 200:
        return {
            "filename": file.filename,
            "virustotal_response": response.json()
        }
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Error when send the file to VirusTotal: {response.text}"
        )
