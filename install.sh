#!/bin/bash

#Instalando e configurando o Postgres
sudo apt-get install postgresql postgresql-contrib



#Instalando o pip
apt-get install python3-pip

#Instalando dependencias
pip install Flask
pip install psycopg2


sudo su postgres
psql
ALTER USER postgres WITH PASSWORD 'postgres';
CREATE DATABASE links;
\c links;

create table users(id_usuario serial primary key,usuario varchar(30) not null unique);

CREATE TABLE links(id serial primary key,hits integer not null,url varchar(100) not null,shorturl varchar(100) not null unique,usuario_id integer not null,FOREIGN KEY (usuario_id) REFERENCES users(id_usuario));
