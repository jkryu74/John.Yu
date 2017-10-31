SELECT * FROM users;
SELECT * FROM comments;
SELECT * FROM messages;

DELETE FROM messages WHERE id = 4;

INSERT INTO messages (id, message, created_at, updated_at)
VALUES (4, "Hello there, we have a luncheon meeting today afternoon. Please be prompt, dress casually, and be ready for some fun!", now(), now());