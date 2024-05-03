-- This file creates a flask_registration_and_login_example schema and the users table within it

create schema if not exists flask_registration_and_login_example character set utf8mb4 collate utf8mb4_general_ci;
use flask_registration_and_login_example;

create table users(
    id int not null auto_increment primary key,
    email varchar(255),
    password varchar(255)
)