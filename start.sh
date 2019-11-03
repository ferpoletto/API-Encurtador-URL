#!/bin/bash

#START NO BANCO DE DADOS
sudo -u postgres psql -h 127.0.0.1 -U postgres -d links

#START NA APLICAÇÃO
python3 run.py