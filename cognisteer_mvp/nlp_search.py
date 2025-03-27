from .query_processor import process_query  # Import our spaCy query processor
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

def search_with_nlp(query_str):
    # Process the user query with spaCy to get a refined version
    refined_query = process_query(query_str)
    print("Refined query:", refined_query)
    
    # Open the Whoosh index from the 'indexdir' folder
    ix = open_dir("indexdir")
    with ix.searcher() as searcher:
        # We'll search the 'content' field for simplicity
        parser = QueryParser("content", schema=ix.schema)
        query = parser.parse(refined_query)
        results = searcher.search(query, limit=10)
        
        # Display search results
        print(f"Found {len(results)} result(s) for the query: '{query_str}'")
        for result in results:
            print("Protocol ID:", result['protocol_id'])
            print("Title:", result['title'])
            # Show the first 200 characters of the content as a snippet
            snippet = result['content'][:200] + "..." if len(result['content']) > 200 else result['content']
            print("Content:", snippet)
            print("=" * 40)

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    search_with_nlp(user_query)
