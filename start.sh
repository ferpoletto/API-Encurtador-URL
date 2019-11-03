#!/bin/bash

#INSTALANDO O PIP E VIRTUALENV
apt-get install python3-pip
sudo apt-get install virtualenv
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt


#START NO BANCO DE DADOS
psql -h 127.0.0.1 -U postgres -d links

#START NA APLICAÇÃO
python3 run.py