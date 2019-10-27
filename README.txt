# Encurtador-URLS-Flask-Postgres

#Para instalar o virtual virtualenv
pip install virtualenv

#Iniciar o virtualenv passando por paramettro a versão do Python que eu quero
virtualenv -p python3 venv

#Ativar o ambiente virtual
. venv/bin/activate

#Criar o arquivo requiriments
venv/bin/pip3 freeze > requirements.txt

#Para instalar as dependencias
venv/bin/pip3 install -r requirements.txt




