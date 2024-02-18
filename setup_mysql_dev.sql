--prepares mysql server
--create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--create user if not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--grant all privillages
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
--grant performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
--Flushing privileges
FLUSH PRIVILEGES;
