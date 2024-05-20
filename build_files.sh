#!/bin/bash

# Instala pip
curl -sSL https://raw.githubusercontent.com/pypa/get-pip/master/get-pip.py | python -

# Atualiza pip
python -m pip install --upgrade pip

# Instala dependências
pip install -r requirements.txt

# Coleta arquivos estáticos
python3.9 manage.py collectstatic --noinput
