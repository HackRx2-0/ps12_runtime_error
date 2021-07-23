CREATE DATABASE recommendation_system;
USE recommendation_system;

CREATE TABLE useraccount (
	id int NOT NULL AUTO_INCREMENT,
	username varchar(50) NOT NULL,
	fname varchar(50) NOT NULL,
	lname varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	mobile varchar(10) NOT NULL,
	pwd varchar(255) NOT NULL,
	cpwd varchar(255) NOT NULL,
	PRIMARY KEY (id)
);

Select * from useraccount;