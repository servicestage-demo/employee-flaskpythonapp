CREATE DATABASE mypolls;

CREATE TABLE mypolls.employee (
    ID VARCHAR(64) NOT NULL PRIMARY KEY,
    firstname VARCHAR(64) NOT NULL,
	lastname VARCHAR(64) NOT NULL,
    gender integer NOT NULL
);

insert into mypolls.employee values (1, "Smith", "John", 0);
insert into mypolls.employee values (2, "Jane", "Swandar", 1);
insert into mypolls.employee values (3, "Bob", "Staney", 0);
