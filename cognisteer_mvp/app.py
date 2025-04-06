from fastapi import HTTPException, FastAPI
from pydantic import BaseModel
from typing import Optional
import logging
from pythonjsonlogger import jsonlogger
from .nlp_search import search_with_nlp  # Ensure search_with_nlp returns a list of dicts

# Set up structured logging
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# Initialize the FastAPI app
app = FastAPI()

# Define the QueryRequest model once
class QueryRequest(BaseModel):
    query: str
    session_id: Optional[str] = None

# GET /health endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Service is running."}

# POST /query endpoint
@app.post("/query")
async def query_protocols(request: QueryRequest):
    try:
        if request.session_id:
            logger.info(f"Session ID: {request.session_id} - Received query: {request.query}")
        results = search_with_nlp(request.query)  # Using our existing search function
        return {"status": "success", "results": results}
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the query.")

# Define FeedbackRequest model (optionally extend with session_id if needed)
class FeedbackRequest(BaseModel):
    feedback: str
    session_id: Optional[str] = None  # Optional session identifier
    details: Optional[str] = None     # Optional additional details

# POST /feedback endpoint
@app.post("/feedback")
def submit_feedback(feedback: FeedbackRequest):
    try:
        if feedback.session_id:
            logger.info("Received feedback for session %s: %s", feedback.session_id, feedback.feedback)
        else:
            logger.info("Received feedback: %s", feedback.feedback)
        
        if feedback.details:
            logger.info("Feedback details: %s", feedback.details)
        
        # In a real application, you might store this feedback in a database or file.
        return {"status": "success", "message": "Feedback received."}
    except Exception as e:
        logger.error("Error processing feedback: %s", str(e))
        raise HTTPException(status_code=500, detail="An error occurred while processing feedback.")