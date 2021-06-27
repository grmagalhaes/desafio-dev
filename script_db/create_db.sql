drop database if exists desafio;
drop user if exists 'desafio'@'localhost';

create database desafio character set utf8;
create user 'desafio'@'localhost' identified by 'desafio123';
grant all privileges on desafio.* to desafio@'localhost';