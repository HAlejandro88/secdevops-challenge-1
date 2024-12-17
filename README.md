# FastAPI VirusTotal 

## Clone the Repository
`git clone `

## Docker Build and Run Instructions

To build and run the application using Docker, follow these steps:

- Build the Docker image without using Docker Compose by running:
    `docker build -t fastapi-virustotal .`

- Run the application container using the following command:
    `docker run -d -p 8000:8000 --env-file .env fastapi-virustotal`
- Once the application is running, you can access the API documentation at:
    `http://localhost:8000/docs`

### Build the Docker with Docker compose

- Compose with the following command:
    `docker-compose build`
- Once the build is complete, you can start the application using Docker Compose:
    `docker-compose up` or `docker-compose up -d` 

To stop the running containers, press Ctrl+C or run:
    `docker-compose down`

## API Documentation
This endpoint allows you to upload a file, save it locally, and send it to VirusTotal for scanning.

Request:

You need to send a POST request to /upload/ with the file as form data.

Key: file
Value: Your file to be uploaded.
Example request in Postman:

Method: POST
URL: http://localhost:8000/upload/
Body: Form-data
Key: file
Value: Select your file to upload
Response: If the file is successfully uploaded and sent to VirusTotal:
```json
{
  "filename": "example_file.txt",
  "virustotal_response": {
    // Response from VirusTotal API
  }
}

```

If there is an error:

```json
{
  "filename": "example_file.txt",
  "message": "Error when send the file to VirusTotal.",
  "status_code": 400,
  "details": "Error details from VirusTotal API"
}

```

## API Key and Environment Variables
You need to set the following environment variables in your .env file:

- VIRUSTOTAL_API_KEY: Your VirusTotal API key.
- UPLOAD_FOLDER: The folder where uploaded files will be saved locally (e.g., /app/uploads).
Example **.env** file:
```bash
VIRUSTOTAL_API_KEY=your_api_key_here
UPLOAD_FOLDER=/app/uploads
```


## Running Locally with Python Environment
If you prefer to run the application locally without Docker, you can do so by following these steps.

- Install Python and Virtual Environment
Make sure you have Python 3.9+ installed on your system. You can check by running:
`python --version`
Then, create and activate a virtual environment:
```bash
python -m venv venv

source venv/bin/activate
```

- Once the virtual environment is activated, install the required dependencies from
`pip install -r requirements.txt`

- Create a .env File
Create a **.env** file in the project root directory to store environment variables. The .env file should look like this:
```bash
VIRUSTOTAL_API_KEY=your_api_key_here
UPLOAD_FOLDER=/app/uploads
```

- Run the Application
Once the dependencies are installed, run the FastAPI application locally with the following command:
`uvicorn main:app --reload`

- Access the Application
    Once the application is running, you can access the API documentation at:
    `http://localhost:8000/docs`
