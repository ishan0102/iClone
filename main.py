import json
import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect("chat.db")

# Run the query
query = """
SELECT
    datetime (message.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime") AS message_date,
    message.text
FROM
    chat
    JOIN chat_message_join ON chat.ROWID = chat_message_join.chat_id
    JOIN message ON chat_message_join.message_id = message.ROWID
WHERE
    chat.chat_identifier = '+12148434974'
    AND message.is_from_me = false
ORDER BY
    message_date ASC;
"""
with conn:
    cursor = conn.execute(query)

# Fetch the results
results = cursor.fetchall()
output_file = "data.json"
with open(output_file, "w") as f:
    json.dump(
        [
            {
                "date": row[0],
                "message": row[1],
            }
            for row in results
        ],
        f,
        indent=4,
    )

print(f"Saved {len(results)} messages to {output_file}")
