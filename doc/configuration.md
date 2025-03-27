# Configuration Settings and Assumptions

## Environment & Dependencies
- **Python Version:** 3.11.x
- **Virtual Environment:** All dependencies are installed in the `venv` directory.
- **Key Dependencies:**
  - FastAPI (v0.115.11)
  - Uvicorn (v0.34.0)
  - spaCy (v3.8.4) with `en_core_web_sm` model
  - Whoosh (v2.7.4)
  - pytest (v8.3.5)
- **Installation Commands:**
  ```bash
  pip install fastapi uvicorn spacy whoosh pytest
  python -m spacy download en_core_web_sm


Directory Structure & File Organization
The project is organized into multiple directories:
cognisteer_mvp/: Contains core backend and NLP modules.
doc/: Contains documentation files.
tests/: Contains unit and integration tests.
protocols/: Contains plain-text protocol files.
indexdir/: Contains Whoosh index files.
venv/: Virtual environment with all dependencies.
This organization facilitates maintainability and clear separation of concerns.
Indexing & NLP Assumptions
Protocol Files:
Protocol files are stored in plain text format under the protocols/ folder.
Filenames encode the protocol ID and title (e.g., protocol_001_introduction.txt).
Indexing Process:
The indexing script (build_index.py) parses the protocols directory, extracts relevant fields, and builds a Whoosh index.
NLP Processing:
spaCy’s en_core_web_sm model is used for tokenization, lemmatization, and refining user queries.
The current query refinement strategy extracts key tokens and joins them with an "OR" operator for search.
API Configuration & Limitations
API Framework:
The API is built using FastAPI and served using Uvicorn.
Endpoints include /health, /query, and /feedback.
Performance Target:
The API is designed to return responses within 2 seconds.
Known Limitations:
No caching mechanism is implemented (caching could be added in future iterations).
The feedback endpoint currently only logs messages and returns a basic acknowledgment.
The system assumes static protocol files; dynamic updates are not yet supported.