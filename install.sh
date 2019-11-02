#!/bin/bash

sudo apt-get update
sudo apt-get install git

cd Documentos
mkdir Projeto
cd Projeto

#Clonando repositório
git clone https://github.com/ferpoletto/Encurtador-URLS-Flask-Postgres.git


#Instalando e configurando o Postgres
sudo apt-get install postgresql postgresql-contrib
sudo su postgres
psql
ALTER USER postgres WITH PASSWORD 'postgres';

create table users(id_usuario serial primary key,usuario varchar(30) not null unique);

CREATE TABLE links(id serial primary key,hits integer not null,url varchar(100) not null,shorturlvarchar(100) not null unique,usuario_id integer not null,FOREIGN KEY (usuario_id)REFERENCES users(id_usuario));

#Instalando o pip
apt-get install python3-pip

#Instalando dependencias
pip install Flask
pip install psycopg2


