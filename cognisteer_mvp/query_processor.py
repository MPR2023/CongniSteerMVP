import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

def process_query(query):
    """
    Process the user query using spaCy to extract key terms.
    This function filters out stop words and punctuation, then returns a refined query string.
    """
    doc = nlp(query)
    # Extract the lemma of tokens that are not stop words or punctuation
    keywords = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    # Join the keywords to form a refined query string
    refined_query = " OR ".join(keywords)
    return refined_query

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    refined = process_query(user_query)
    print("Refined query:", refined)