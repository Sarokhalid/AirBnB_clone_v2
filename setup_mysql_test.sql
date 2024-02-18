-- prepares mysql server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user if not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privillages
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- grant performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
-- Flushing privileges
FLUSH PRIVILEGES;
