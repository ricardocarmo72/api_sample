# api_sample
Projeto Teste API

Este projeto visa demonstrar a construção de uma API para persistência de números de cartões.
Foi desenvolvido em Python, juntamente com os frameworks Django e Django Rest Framework.

Para executar localmente, siga os passos abaixo:

1. Clone o repositório:<br>
```git clone git@github.com:ricardocarmo72/api_sample.git```

2. Ative o ambiente virtual:<br>
Se estiver usando Windows, apenas ative a env que está na pasta env e pule para o passo 3:<br>
```env\scripts\activate```<br>
Se estiver usando Linux, crie e ative uma env utilizando uma versão do Python igual ou superior a 3.8:<br>
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

Para rodar os testes, digite:<br>
```python manage.py test```

A aplicação expõe dois endpoints:

End-point para autenticação do usuário:<br>
Deve ser executado via <b>POST</b>: ```http://localhost:8000/token/```<br>
Exemplo:<br>
```    
curl --location 'http://localhost:8000/token/' \
    --form 'username="ricardo"' \
    --form 'password="123mudar"'
```
<br>

Este endpoint retorna um access token que pode ser utilizado no outro endpoint, descrito a seguir:<br>

7. Para consultar um card:<br>
Deve ser executado via <b>GET</b>: ```http://localhost:8000/api/?card_number=1234567890```<br>

8. Para inserir um único card:<br>
Deve ser executado via <b>POST</b>: ```http://localhost:8000/api/```<br>
Exemplo de payload:<br>
```{"insert_mode": "single", "card_number": "1234567890"}```

9. Para consultar um card number:<br>
Deve ser executado via <b>GET</b>: ```http://localhost:8000/api/```<br>
Exemplo de payload:<br>
```{"card_number": "1234567890"}```<br>
A requisição deve informar o token de autenticação no header:
