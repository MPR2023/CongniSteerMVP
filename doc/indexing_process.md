# Indexing Process

This document explains how the system indexes the protocol files using Whoosh.

## Overview
- The `build_index.py` script (located in `cognisteer_mvp/`) scans the `protocols/` directory for `.txt` files.
- Each file is parsed to extract:
  - **Protocol ID:** Derived from the filename (e.g., `protocol_001_introduction`).
  - **Title:** Also derived from the filename, with underscores replaced by spaces.
  - **Content:** The full text from the `.txt` file.

## Steps

1. **Define Schema:**  
   - In `build_index.py`, we create a Whoosh schema with fields for `protocol_id`, `title`, and `content`.

2. **Create/Open the Index Directory:**  
   - The script checks if `indexdir/` exists.
   - If not, it creates the directory and initializes a new Whoosh index with the defined schema.
   - If `indexdir/` already exists, it opens the existing index.

3. **Traverse Protocol Files:**
   - The script loops through each workspace folder inside `protocols/`.
   - For each `.txt` file, it reads the content and extracts:
     - `protocol_id`: The portion of the filename before `.txt`.
     - `title`: A user-friendly version of the filename (underscores replaced with spaces).
     - `content`: The entire file text.

4. **Write Documents to the Index:**
   - A Whoosh writer is created, and each file is added as a new document with the fields defined in the schema.
   - After all files are processed, the writer is committed to save changes.

5. **Result:**
   - The `indexdir/` folder now contains the Whoosh index files.
   - Subsequent search operations use these index files to quickly locate relevant protocols.

## Sample Code Snippet

```python
# build_index.py
schema = Schema(
    protocol_id=ID(stored=True, unique=True),
    title=TEXT(stored=True),
    content=TEXT(stored=True)
)

# Create/Open index
if not os.path.exists(index_dir):
    os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)
else:
    ix = index.open_dir(index_dir)

writer = ix.writer()
# Traverse protocols
for workspace in os.listdir(protocols_dir):
    # ...
    # Add documents
    writer.add_document(protocol_id=protocol_id, title=title, content=content)
writer.commit()
