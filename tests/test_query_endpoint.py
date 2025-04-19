from fastapi.testclient import TestClient
from cognisteer_mvp.app import app  # Adjust this import if your module structure differs

client = TestClient(app)

def test_area_mapping_found():
    payload = {
        "query": "Fetch protocol for Security Zone",
        "area": "Security Zone",
        "session_id": "exampleSession"
    }
    response = client.post("/query", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    # Check that results is a list with one mapping and that its protocol_id matches the expected value
    assert isinstance(data["results"], list)
    mapping = data["results"][0]
    assert mapping["protocol_id"] == "protocol_001"
    # You can also check title and content if needed:
    assert mapping["title"] == "Security Protocol for Security Zone"


def test_area_mapping_not_found_fallback():
    payload = {
        "query": "Some general query",
        "area": "Unknown Zone",
        "session_id": "exampleSession"
    }
    response = client.post("/query", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    # Since it falls back to NLP search, results should come from search_with_nlp.
    # Depending on your search_with_nlp function, you might check that the results list is not empty.
    assert isinstance(data["results"], list)
    # Optionally, check that the results do not contain a protocol mapping for "Security Zone"
    # (This may vary based on your implementation of search_with_nlp.)