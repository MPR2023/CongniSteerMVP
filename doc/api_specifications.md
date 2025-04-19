API Endpoint Specifications
This document outlines the available API endpoints, their request/response formats, and sample usage.

Overview
The API is built using FastAPI.

It runs on http://127.0.0.1:8000 by default when you execute:

bash
Copy
uvicorn cognisteer_mvp.app:app --reload
The API is designed to respond within 2 seconds. Future enhancements may include caching with Redis, authentication, and advanced query parsing.

Endpoints
GET /health
Description:
Confirms that the backend service is operational.

Method: GET

URL:
http://127.0.0.1:8000/health

Sample Request (using curl):

bash
Copy
curl -X GET http://127.0.0.1:8000/health
Sample Response:

json
Copy
{
  "status": "ok",
  "message": "Service is running."
}
POST /query
Description:
Accepts a natural language query along with an explicit area identifier, processes it using spaCy and Whoosh, and returns matching protocol data. If the area field (e.g., "Security Zone") is provided and found in the centralized mapping, the corresponding protocol is returned directly. Otherwise, the query is processed with NLP as a fallback.

Method: POST

URL:
http://127.0.0.1:8000/query

Request Model:
The QueryRequest model now has the following structure:

json
Copy
{
  "query": "Fetch protocol for Security Zone",
  "area": "Security Zone",
  "session_id": "exampleSession"  // (Optional)
}
query: The user's text query.

area: A required field representing the area identifier (e.g., "Security Zone").
When this field matches an existing mapping, the backend returns the associated protocol.

session_id: An optional identifier for tracking the session.

Sample Request (using curl):

bash
Copy
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{
  "query": "Fetch protocol for Security Zone",
  "area": "Security Zone",
  "session_id": "exampleSession"
}'
Sample Response (when area is recognized):

json
Copy
{
  "status": "success",
  "results": [
    {
      "protocol_id": "protocol_001",
      "title": "Security Protocol for Security Zone",
      "content": "Detailed security protocol guidance content here..."
    }
  ]
}
Fallback Behavior:
If the provided area is not found in the mapping, the endpoint falls back to processing the query using the NLP search (via spaCy and Whoosh), returning the corresponding search results.

Error Handling:
If an error occurs (e.g., unknown area without fallback data, processing error), the endpoint returns an HTTP 500 response with a JSON error message indicating that an error occurred while processing the query.

POST /feedback
Description:
Collects user feedback or error logs from the mobile application.

Method: POST

URL:
http://127.0.0.1:8000/feedback

Request Model:
Example payload:

json
Copy
{
  "feedback": "The response was slow.",
  "session_id": "exampleSession",  // Optional
  "details": "API call timed out after 2 seconds."  // Optional
}
Sample Request (using curl):

bash
Copy
curl -X POST "http://127.0.0.1:8000/feedback" -H "Content-Type: application/json" -d '{
  "feedback": "The response was slow.",
  "session_id": "exampleSession",
  "details": "API call timed out after 2 seconds."
}'
Sample Response:

json
Copy
{
  "status": "success",
  "message": "Feedback received."
}
Integration in the Project
Modular Design:
The mobile application sends a structured JSON payload with the fields query, area, and (optionally) session_id.

If the area (e.g., "Security Zone") matches an entry in our central protocol mapping, the backend returns the mapped protocol data.

Otherwise, the natural language query is processed using our NLP pipeline.

Logging and Error Handling:
All critical events and errors are logged using structured JSON logging (via python-json-logger), ensuring that any issues during processing are captured for debugging.

Future Enhancements:
Potential improvements include integrating a database for dynamic protocol mapping, caching frequently used queries, and adding authentication to secure API endpoints.

Version Control:
This documentation is version-controlled and referenced in the project README for future developers.