-- CREATE DATABASE flask_db;
-- CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'flasksenha';
-- GRANT ALL PRIVILEGES ON flask_db.* TO 'flask_user'@'localhost';
-- FLUSH PRIVILEGES;

-- ALTER USER 'flask_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'flasksenha';
-- FLUSH PRIVILEGES;

-- SELECT User, Host FROM mysql.user;

-- CREATE USER 'flask_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'flasksenha';
-- GRANT ALL PRIVILEGES ON flask_db.* TO 'flask_user'@'localhost';
-- FLUSH PRIVILEGES;

SHOW GRANTS FOR 'flask_user'@'localhost';

GRANT ALL PRIVILEGES ON flask_db.* TO 'flask_user'@'localhost';
FLUSH PRIVILEGES;

USE flask_db;
ALTER TABLE usuarios MODIFY senha_hash VARCHAR(255);