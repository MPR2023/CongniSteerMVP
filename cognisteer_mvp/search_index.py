from whoosh.index import open_dir
from whoosh.qparser import QueryParser

def search_protocols(query_str):
    # Open the index directory
    ix = open_dir("indexdir")
    # Create a searcher object
    with ix.searcher() as searcher:
        # We'll search the 'content' field; adjust as needed (or add multiple fields)
        parser = QueryParser("content", schema=ix.schema)
        query = parser.parse(query_str)
        results = searcher.search(query, limit=10)
        
        # Print out the search results
        print(f"Found {len(results)} result(s) for query: '{query_str}'")
        for result in results:
            print("Protocol ID:", result['protocol_id'])
            print("Title:", result['title'])
            # Print a snippet of the content (first 200 characters)
            snippet = result['content'][:200] + "..." if len(result['content']) > 200 else result['content']
            print("Content:", snippet)
            print("=" * 40)

if __name__ == "__main__":
    query_str = input("Enter your search query: ")
    search_protocols(query_str)
