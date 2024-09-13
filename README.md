# Pré-requisitos:

## Instalação do Python:

Necessario ter o python instaldo cado queira roda na sua maquina.

Crie um diretório vazio onde você deseja armazenar seu projeto Django.


Execute o seguinte comando para criar um novo projeto Django:

```

django-admin startproject setup .
```

Este comando irá gerar os arquivos e diretórios básicos para o seu projeto Django, incluindo setup.py, e uma estrutura de pastas para seus aplicativos. manage.py


## Executando o Projeto Django:

### Crie um ambiente virtual (opcional, mas recomendado):

É recomendável usar um ambiente virtual para isolar as dependências do seu projeto das suas outras instalações Python.
Você pode usar ferramentas como virtualenv ou venv para criar um ambiente virtual. Consulte a documentação da ferramenta escolhida para obter instruções sobre como criar e ativar o ambiente virtual.
Instale as dependências do projeto:

Navegue até o diretório principal do seu projeto no terminal.

Ative o ambiente virtual (se criado).

### Execute o seguinte comando para instalar as dependências do projeto:

```
pip install -r requirements.txt
```

Este comando lerá o arquivo requirements.txt (gerado durante a criação do projeto) e instalará as dependências necessárias.

## Execute o servidor de desenvolvimento:

### Execute o seguinte comando para iniciar o servidor de desenvolvimento Django:

```
python manage.py runserver
```

Isso iniciará um servidor local na porta 8000. Você poderá acessar seu aplicativo em http://localhost:8000/ em seu navegador.


## Criar migrations:

### Execute o seguinte comando para gerar migrations para suas alterações no modelo de dados:

```
python manage.py makemigrations

```

## Aplicar migrations:

### Execute o seguinte comando para aplicar as migrations geradas ao seu banco de dados:

```

python manage.py migrate
```

## Criar novo aplicativo:

### Execute o seguinte comando para criar um novo aplicativo Django:

```
python manage.py startapp myapp

```

## Substitua myapp pelo nome desejado para o seu aplicativo.

### Executar testes:

Execute o seguinte comando para executar os testes do seu projeto:

```
python manage.py test

```

# Observações: Para rodar no Docker:

```
docker-compose build 

```

```
docker-compose up 
```

# Isso cira o super Usuario no Django

```
 python manage.py createsuperuser 
```

## Admin 

```
http://localhost:8000/admin/
```
Senha e Username criados para o super user
```
admin
```
```
Admin123.
```

Depois que for criado o super usuario tera acesso ao User admin, aos cruds e coisas criadas.

Atenção: Tudo isso pode ser acessado pelo link acima, pois esta rodando no docker;