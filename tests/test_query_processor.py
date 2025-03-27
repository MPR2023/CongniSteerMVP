import sys
import os
# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cognisteer_mvp.query_processor import process_query

def test_process_query():
    # Example query
    input_query = "How do I ensure safety during maintenance procedures?"
    refined = process_query(input_query)
    # We expect the refined query to contain these keywords
    expected_keywords = ["ensure", "safety", "maintenance", "procedure"]
    for keyword in expected_keywords:
        assert keyword in refined, f"Expected '{keyword}' to be in the refined query, but got: {refined}"