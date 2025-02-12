from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from crewai import Crew, Process
from agents import junior_sales_associate, senior_sales_associate
from tasks import lead_ranking, communication_generation
import os
import logging
from tempfile import NamedTemporaryFile
import shutil

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="CrewAI Sales API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Default Vite React app port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_crew() -> Crew:
    """Create a new Crew instance"""
    lead_ranking.agent = junior_sales_associate
    communication_generation.agent = senior_sales_associate
    
    return Crew(
        agents=[junior_sales_associate, senior_sales_associate],
        tasks=[lead_ranking, communication_generation],
        process=Process.sequential,
        verbose=True
    )

@app.post("/process")
async def process_file(file: UploadFile = File(...)):
    """
    Process the uploaded CSV file with CrewAI
    """
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )

    try:
        # Create a temporary file to store the uploaded CSV
        with NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
            # Copy the uploaded file to the temporary file
            shutil.copyfileobj(file.file, temp_file)
            temp_path = temp_file.name

        try:
            crew = create_crew()
            result = crew.kickoff(inputs={"file_path": temp_path})
            return {"status": "success", "result": result}
        finally:
            # Clean up the temporary file
            os.unlink(temp_path)

    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )
    finally:
        file.file.close()

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.get("/")
async def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to the CrewAI Sales API!",
        "version": "1.0.0",
        "endpoints": {
            "/process": "POST - Process a CSV file with CrewAI",
            "/health": "GET - Check API health"
        }
    }