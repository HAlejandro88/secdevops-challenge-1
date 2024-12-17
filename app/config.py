import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    VIRUSTOTAL_API_KEY: str = os.getenv("VIRUSTOTAL_API_KEY")
    VIRUSTOTAL_API_URL: str = "https://www.virustotal.com/vtapi/v2/file/scan"
    UPLOAD_FOLDER: str = os.getenv("UPLOAD_FOLDER", "./uploads")

# Crear una instancia de Settings
settings = Settings()
