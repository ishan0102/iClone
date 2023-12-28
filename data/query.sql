-- query.sql
WITH MessageDetails AS (
    SELECT
        m.ROWID, m.text, m.date, chj.chat_id, m.is_from_me,
        LEAD(m.is_from_me, 1) OVER (PARTITION BY chj.chat_id ORDER BY m.date) AS next_is_from_me,
        LEAD(m.text, 1) OVER (PARTITION BY chj.chat_id ORDER BY m.date) AS next_text,
        LEAD(m.date, 1) OVER (PARTITION BY chj.chat_id ORDER BY m.date) AS next_date
    FROM
        message AS m
        JOIN chat_message_join AS chj ON m.ROWID = chj.message_id
        JOIN chat ON chj.chat_id = chat.ROWID
    WHERE
        chat.chat_identifier = '{phone_number}'
        AND m.text IS NOT NULL
)

SELECT
    text AS my_message,
    next_text AS other_person_message
FROM
    MessageDetails
WHERE
    is_from_me = 1 AND next_is_from_me = 0
ORDER BY
    date;
