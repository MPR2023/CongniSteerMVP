from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
import logging
from .nlp_search import search_with_nlp  # Ensure your nlp_search.py's search_with_nlp returns results as a list of dicts

# Set up basic logging (logs will be printed in a simple format)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Initialize the FastAPI app
app = FastAPI()

# GET /health endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Service is running."}
class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_protocols(request: QueryRequest):
    try:
        # Use the search function to process the query and retrieve results
        results = search_with_nlp(request.query)
        return {"status": "success", "results": results}
    except Exception as e:
        logging.error("Error processing query: %s", str(e))
        raise HTTPException(status_code=500, detail="An error occurred while processing the query.")
    
class FeedbackRequest(BaseModel):
    feedback: str
    # Optionally, you can add other fields, e.g., session_id, timestamp, etc.
    # session_id: Optional[str] = None
    
@app.post("/feedback")
def submit_feedback(feedback: FeedbackRequest):
    try:
        # For now, just log the feedback
        logging.info("Received feedback: %s", feedback.feedback)
        # In a real application, you might store this in a database or file
        return {"status": "success", "message": "Feedback received."}
    except Exception as e:
        logging.error("Error processing feedback: %s", str(e))
        raise HTTPException(status_code=500, detail="An error occurred while processing feedback.")