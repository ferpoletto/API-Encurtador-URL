#!/bin/bash

#Instalando e configurando o Postgres
sudo apt-get install postgresql postgresql-contrib

sudo -u postgres psql

sudo -u postgres psql -d postgres -c "ALTER USER postgres PASSWORD 'postgres';"

sudo -u postgres psql -d postgres -c create database links;

sudo -u postgres psql -d postgres -c \c links;

sudo -u postgres psql -d postgres -c create table users(id_usuario serial primary key,usuario varchar(30) not null unique);

sudo -u postgres psql -d postgres -c CREATE TABLE links(id serial primary key,hits integer not null,url varchar(100) not null,shorturl varchar(100) not null unique,usuario_id integer not null,FOREIGN KEY (usuario_id) REFERENCES users(id_usuario));

#Instalando o pip
apt-get install python3-pip

#Instalando dependencias
pip install Flask
pip install psycopg2



