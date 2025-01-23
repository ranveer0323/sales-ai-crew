from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crewai import Crew, Process
from agents import junior_sales_associate, senior_sales_associate
from tasks import lead_ranking, communication_generation
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="CrewAI Sales API", version="1.0.0")


class FileInput(BaseModel):
    file_path: str


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


@app.post("/kickoff")
async def kickoff(input_data: FileInput):
    """
    Process the input file with CrewAI
    """
    if not os.path.exists(input_data.file_path):
        raise HTTPException(
            status_code=400,
            detail=f"File path does not exist: {input_data.file_path}"
        )

    try:
        crew = create_crew()
        result = crew.kickoff(inputs={"file_path": input_data.file_path})
        return {"status": "success", "result": result}
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )


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
            "/kickoff": "POST - Start a new crew task",
            "/health": "GET - Check API health"
        }
    }
