BANCO DE DADOS
1 - sudo apt-get update
2 - sudo apt-get install postgresql postgresql-contrib

3 - sudo su postgres
4 - psql
5 - ALTER USER postgres WITH PASSWORD 'postgres';

6 - CREATE TABLE links (
id serial primary key,
hits integer not null,
url varchar(200) not null,
shorturl varchar(100) not null unique
);

PROJETO:
7 - Clonar o projeto;
8 - Instalar os requirements.txt
9 - Rodar o arquivo run.py



