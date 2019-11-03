#!/bin/bash

#START NO BANCO DE DADOS
#sudo -u postgres psql -h postgres -U postgres -d links

#START NA APLICAÇÃO
source venv/bin/activate
python3 run.py
