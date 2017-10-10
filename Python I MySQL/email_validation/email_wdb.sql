SELECT * FROM emails;

INSERT INTO valid_email (email, created_at, updated_at)
VALUES ("kangkang@hmail.com", NOW(), NOW());

DELETE FROM emails
WHERE id = 5;