#!/bin/bash

# Baixa e instala o pip
curl -sSL https://bootstrap.pypa.io/get-pip.py | python3.9 -

# Atualiza o pip para a última versão
python3.9 -m pip install --upgrade pip

# Instala as dependências do projeto
python3.9 -m pip install -r requirements.txt

# Coleta os arquivos estáticos
python3.9 manage.py collectstatic --noinput
