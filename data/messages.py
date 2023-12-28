import json
import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect("chat.db")

# Run the query
query = """
SELECT
    message.text
FROM
    chat
    JOIN chat_message_join ON chat.ROWID = chat_message_join.chat_id
    JOIN message ON chat_message_join.message_id = message.ROWID
WHERE
    chat.chat_identifier = '+12148434974'
    AND message.is_from_me = false
    AND message.text IS NOT NULL
ORDER BY
    message_date ASC;
"""
with conn:
    cursor = conn.execute(query)

# Split into train, valid, test (80/10/10)
results = cursor.fetchall()
train_size = int(0.8 * len(results))
valid_size = int(0.1 * len(results))
test_size = len(results) - train_size - valid_size
datasets = [
    (results[:train_size], "train"),
    (results[train_size : train_size + valid_size], "valid"),
    (results[train_size + valid_size :], "test"),
]

for dataset, name in datasets:
    with open(f"data/{name}.jsonl", "w") as f:
        for row in dataset:
            json.dump({"text": row[0]}, f)
            f.write("\n")
