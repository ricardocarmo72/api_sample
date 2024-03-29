# Projeto Teste API

Este projeto visa demonstrar a construção de uma API para persistência de números de cartões.
Foi desenvolvido em Python, juntamente com os frameworks Django e Django Rest Framework.

Para executar localmente, siga os passos abaixo:

1. Clone o repositório:<br>
```git clone git@github.com:ricardocarmo72/api_sample.git```

2. Ative o ambiente virtual:<br>
Se estiver usando <b>Windows</b>, ative a env que está na pasta env com o comando:<br>
```env\scripts\activate```<br>
Se estiver usando <b>Linux</b>, crie e ative uma env utilizando uma versão do Python igual ou superior a 3.8:<br>
```python3 -m venv env```<br>
```source env/bin/activate```<br>
Em seguida instale as bibliotecas requeridas:<br>
```pip install -r src/requirements.txt```<br>

3. Crie um banco de dados PostgreSQL com o nome ```hyperativa``` via PgAdmin ou outra ferramenta.

4. Acesse a pasta src no terminal e rode as migrações:<br>
```cd src```<br>
```python manage.py migrate```<br>

5. Crie um usuário superuser:<br>
```python manage.py createsuperuser```

6. Suba a aplicação:<br>
```python manage.py runserver```

<h3>Testes</h3>

Para rodar os testes, digite:<br>
```python manage.py test```

<h3>Documentação</h3>

A documentação (contratos da API) pode ser conferida via Swagger:<br>
```http://localhost:8000/swagger/```<br>

A aplicação expõe dois endpoints:<br>

<h3>End-point para autenticação do usuário:</h3>

- Deve ser executado via <b>POST</b>:<br>
```http://localhost:8000/token/```<br>
Exemplo de payload (Deve ser passado o mesmo usuário/senha usado no passo 5 acima):<br>
```{"username": "test_user", "password": "test123"}```<br>

Este endpoint retorna um <em>access token</em> que pode ser utilizado no outro endpoint, descrito a seguir:<br>

(<u>Em todos os requests abaixo, o token de autenticação deve ser passado no header como Bearer token</u>)<br>

<h3>End-point para consulta de dados</h3>

Deve ser executado via <b>GET</b>:<br>
```http://localhost:8000/api/?card_number=1234567890```<br>

<h3>End-point para inserção de dados</h3>

- Para inserir um único card:<br>
Deve ser executado via <b>POST</b>:<br>
```http://localhost:8000/api/```<br>
Exemplo de payload:<br>
```{"insert_mode": "single", "card_number": "1234567890"}```

- Para inserir vários cards a partir de um arquivo .TXT:<br>
Deve ser executado via <b>POST</b>:<br>
```http://localhost:8000/api/```<br>
Exemplo de payload:<br>
```{"insert_mode": "multiple", "file_uploaded": <arquivo>}```

(Utilizar o arquivo .TXT existente na pasta raiz do projeto)

<h3>Logs das requisições</h3>
Foi implementado via middleware, exibindo o log no console do terminal. Pode ser facilmente adaptado para persistir em banco ou integrar com outras ferramentas, como ELK, New Relic, etc.

<h3>Postman</h3>
Para facilitar os testes com a API, foi adicionado o arquivo Hyperativa.postman_collection.json na pasta raiz do projeto.
Basta importar no Postman e acessar os endpoints da coleção.
