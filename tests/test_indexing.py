import os
from whoosh.index import open_dir

def test_index_document_count():
    """
    Verify that the index contains the expected number of documents.
    Based on our protocol folder structure, we expect 10 documents.
    """
    index_dir = "indexdir"
    
    # Ensure the index directory exists
    assert os.path.exists(index_dir), "Index directory does not exist. Please run build_index.py first."
    
    # Open the index
    ix = open_dir(index_dir)
    with ix.searcher() as searcher:
        doc_count = searcher.doc_count()
        # We expect 10 documents (5 from each workspace)
        assert doc_count == 10, f"Expected 10 documents in index, but found {doc_count}"
