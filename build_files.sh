curl -sSL https://raw.githubusercontent.com/pypa/get-pip/master/get-pip.py | python -
python -m pip install --upgrade pip
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput