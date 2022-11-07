-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- create table states (id INT unique, auto generated, can’t be null and is a primary key)
CREATE TABLE IF NOT EXISTS states(
    UNIQUE(id),
	id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(id),
    name VARCHAR(256) NOT NULL
);
