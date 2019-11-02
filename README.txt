BANCO DE DADOS
1 - sudo apt-get update
2 - sudo apt-get install postgresql postgresql-contrib

3 - sudo su postgres
4 - psql
5 - ALTER USER postgres WITH PASSWORD 'postgres';

6 -create table users(
id_usuario serial primary key,
usuario varchar(30) not null unique);


CREATE TABLE links(
id serial primary key,
hits integer not null,
url varchar(100) not null,
shorturl varchar(100) not null unique,
usuario_id integer not null,
FOREIGN KEY (usuario_id) REFERENCES users(id_usuario));

PROJETO:
7 - Clonar o projeto;
8 - Instalar os requirements.txtd
9 - Rodar o arquivo run.py







