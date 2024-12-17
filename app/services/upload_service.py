import httpx
from app.config import settings

async def scan_file_with_virustotal(file_path: str, file_name: str):
    async with httpx.AsyncClient() as client:
        with open(file_path, "rb") as file_to_scan:
            response = await client.post(
                settings.VIRUSTOTAL_API_URL,
                files={"file": (file_name, file_to_scan)},
                data={"apikey": settings.VIRUSTOTAL_API_KEY}
            )
    return response
