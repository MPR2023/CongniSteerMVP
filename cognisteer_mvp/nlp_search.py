from .query_processor import process_query  # Import our spaCy query processor
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

def search_with_nlp(query_str):
    # Process the user query with spaCy to get a refined version
    refined_query = process_query(query_str)
    print("Refined query:", refined_query)
    
    # Open the Whoosh index from the 'indexdir' folder
    ix = open_dir("indexdir")
    results_list = []  # Create a list to store the results
    with ix.searcher() as searcher:
        # We'll search the 'content' field for simplicity
        parser = QueryParser("content", schema=ix.schema)
        query = parser.parse(refined_query)
        results = searcher.search(query, limit=10)
        
        print(f"Found {len(results)} result(s) for the query: '{query_str}'")
        for result in results:
            # Generate a snippet for the content
            snippet = result['content'][:200] + "..." if len(result['content']) > 200 else result['content']
            result_dict = {
                "protocol_id": result["protocol_id"],
                "title": result["title"],
                "content": snippet
            }
            results_list.append(result_dict)
            
            print("Protocol ID:", result['protocol_id'])
            print("Title:", result['title'])
            print("Content:", snippet)
            print("=" * 40)
    
    return results_list

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    results = search_with_nlp(user_query)
    print("Returned results:", results)