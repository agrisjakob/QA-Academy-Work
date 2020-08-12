CREATE DATABASE chaperootodo;
CREATE table chaperootodo.todo (
    task_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    task    varchar(255) NOT NULL,
    priority int NOT NULL,
    status  char(10) NOT NULL
);
