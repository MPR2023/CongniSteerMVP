# protocol_mapping.py
# Read the safety protocol from the text file
with open(r"C:\Users\paulm\Desktop\cogniSteer_MVP\protocols\workspace1\protocol_002_safety.txt", "r", encoding="utf-8") as f:
    safety_protocol_content = f.read()
# This dictionary maps area identifiers to their corresponding protocol details.
protocol_mapping = {
    "Security Zone": {
        "protocol_id": "protocol_002",
        "title": "Safety Protocol for Security Zone",
        "content": safety_protocol_content  # This now contains the file content
    },
    # You can add additional mappings for other areas as needed.
    # "Some Other Area": {
    #     "protocol_id": "protocol_002",
    #     "title": "Another Protocol Title",
    #     "content": "Detailed protocol content for this area..."
    # }
}