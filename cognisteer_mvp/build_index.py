import os
from whoosh import index
from whoosh.fields import Schema, TEXT, ID

# Define the schema: protocol_id, title, and content
schema = Schema(
    protocol_id=ID(stored=True, unique=True),
    title=TEXT(stored=True),
    content=TEXT(stored=True)
)

# Specify the directory to store the index
index_dir = "indexdir"

# Create the index directory if it doesn't exist; otherwise, open it
if not os.path.exists(index_dir):
    os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)
else:
    ix = index.open_dir(index_dir)

# Define the protocols directory path (it should be in your project folder)
protocols_dir = "protocols"

# Start the indexing process by creating a writer
writer = ix.writer()

# Traverse each workspace folder in protocols
for workspace in os.listdir(protocols_dir):
    workspace_path = os.path.join(protocols_dir, workspace)
    if os.path.isdir(workspace_path):
        for filename in os.listdir(workspace_path):
            if filename.endswith(".txt"):
                filepath = os.path.join(workspace_path, filename)
                # Extract protocol ID from the filename (remove extension)
                protocol_id = filename.split('.')[0]
                # Derive title from the filename (you can adjust this as needed)
                title = filename.replace("_", " ").split(".")[0]
                # Read the full content of the file
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                print(f"Indexing file: {filepath}")
                writer.add_document(protocol_id=protocol_id, title=title, content=content)

# Commit the changes to save the index
writer.commit()
print("Indexing complete!")
