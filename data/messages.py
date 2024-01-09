import json
import re
import sqlite3


def preprocess_message(text):
    text = re.sub(r"http\S+", "<URL>", text)  # Replace URLs with a placeholder
    text = text.replace("\ufffc", "<ATTACHMENT>")  # Replace non-text content placeholder
    text = (
        text.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    )  # Normalize quotes
    text = re.sub(r"\s+", " ", text).strip()  # Trim extra whitespaces and whitespace characters
    return text


# Connect to your SQLite database
conn = sqlite3.connect("chat.db")

# Define the phone number
phone_number = 0

# Read the SQL query from the file and format it with the phone number
with open("data/query.sql", "r") as file:
    query = file.read().format(phone_number=phone_number)

# Execute the query
with conn:
    cursor = conn.execute(query)

# Clean and preprocess data
results = []
for row in cursor:
    my_message, other_person_message = row
    if my_message and other_person_message:  # Skip if either message is empty
        my_message = preprocess_message(my_message)
        other_person_message = preprocess_message(other_person_message)
        if len(my_message) <= 100 and len(other_person_message) <= 100:  # Skip if either message is too long
            results.append((my_message, other_person_message))

# Split into train and valid sets (90/10)
train_size = int(0.9 * len(results))
valid_size = len(results) - train_size
datasets = [
    (results[:train_size], "train"),
    (results[train_size:], "valid"),
]

# Save the datasets
for dataset, name in datasets:
    with open(f"data/{name}.jsonl", "w") as f:
        for row in dataset:
            json.dump({"text": f"Me: {row[0]}\nPerson: {row[1]}"}, f)
            f.write("\n")
    print(f"Saved {len(dataset)} messages to data/{name}.jsonl")
