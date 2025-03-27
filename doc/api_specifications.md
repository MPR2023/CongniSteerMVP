# API Endpoint Specifications

This document outlines the available API endpoints, their request/response formats, and sample usage.

## Overview
- The API is built using [FastAPI](https://fastapi.tiangolo.com/).
- It runs on `http://127.0.0.1:8000` by default when you execute:
  ```bash
  uvicorn cognisteer_mvp.app:app --reload


Endpoint Details for Each Route:

GET /health:

Description: Explain that this endpoint confirms the backend is operational.
Method: GET
URL: http://127.0.0.1:8000/health
Sample Request: (e.g., using curl)
Sample Response: Provide the JSON output, such as:
json
Copy
{ "status": "ok", "message": "Service is running." }
POST /query:

Description: Describe that this endpoint accepts a query, processes it using spaCy and Whoosh, and returns matching protocol data.
Method: POST
URL: http://127.0.0.1:8000/query
Request Model: Show the Pydantic model (e.g., {"query": "Your query here"}).
Sample Request: Provide an example using curl or similar.
Sample Response: Include a sample JSON response showing at least one protocol result.
Error Handling: Note what happens if there's an error (e.g., HTTP 500 with a JSON error message).
POST /feedback (Optional):

Description: Explain that this endpoint collects user feedback or error logs.
Method: POST
URL: http://127.0.0.1:8000/feedback
Request Model: Show the expected payload (e.g., {"feedback": "..."}).
Sample Request and Response: Provide examples.
Performance & Future Enhancements:

Mention that the API is designed to respond within 2 seconds.
Include notes on potential future enhancements like caching with Redis, authentication, or advanced query parsing.
Formatting and Clarity:

Use Markdown headings and code blocks to keep the file organized.
Include any necessary diagrams or links if you have them (optional).
Integration in the Project:

Once completed, ensure this documentation is version-controlled (commit it to Git) and referenced in your README file for future developers.