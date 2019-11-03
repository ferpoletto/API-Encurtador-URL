#!/bin/bash

#INSTALANDO O GIT
sudo apt-get update
sudo apt-get install git
#sudo apt-get upgrade python3

#INSTALANDO DEPENDENCIAS
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install libpq-dev python-dev

#INSTALANDO E CONFIGURANDO O POSTGRES
postgresql-setup initdb
sudo -u postgres createdb links
sudo -u postgres psql -d postgres -c "ALTER USER postgres WITH PASSWORD 'postgres'"
sudo -u postgres psql -d postgres -c "CREATE TABLE users (id_usuario serial primary key,usuario varchar(30) not null unique)";
sudo -u postgres psql -d postgres -c "CREATE TABLE links (id serial primary key,hits integer not null,url varchar(100) not null,shorturl varchar(100) not null unique,usuario_id integer not null,FOREIGN KEY (usuario_id) REFERENCES users(id_usuario))";




