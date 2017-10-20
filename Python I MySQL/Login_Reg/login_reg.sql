SELECT * FROM login;

INSERT INTO login (first_name, last_name, email, password, conf_pw, created_at, updated_at)
VALUES ("Michael", "Hardaway", "login@email.com", "secretpw101", "secretpw101", now(), now());

INSERT INTO login (first_name, last_name, email, password, conf_pw, created_at, updated_at)
VALUES ("Tim", "Lampo", "TLpo@hmail.com", "password23", "password23", now(), now());

UPDATE login SET user_name="logginData" WHERE id=2;
