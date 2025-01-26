CREATE DATABASE docker_containers_db;
USE docker_containers_db;
CREATE TABLE docker_containers_table (
CONTAINRER_ID VARCHAR(13), 
IMAGE VARCHAR(20),
NAME VARCHAR(20)
);
INSERT INTO docker_containers_table 
VALUES('605adf483577', 'mariadb', 'mariadb-test'),
('582c5cdbe01d', 'mysql', 'mysql-test'),
('e09e0b567f53', 'postgres', 'postgres-test');
