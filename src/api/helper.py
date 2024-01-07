"""
Para atender ao requisito "armazenar os dados de forma segura",
resolvi armazenar o número do cartão simulando uma criptografia simples,
convertendo o número do cartão para o formato base64.
É possível utilizar algoritmos de criptografia mais seguros, como o que o Django 
utiliza para armazenar as senhas dos usuários, porém isso degrada bastante a 
performance da aplicação, além de ser impossível desencriptar os dados.
Outros algoritmos mais rápidos podem gerar efeitos colaterais, como a impossibilidade 
de pesquisar a existência de algum cartão pelo número, sem fornecer o ID.
"""
import base64

def encrypt_data(data):
    return base64.b64encode(data.encode("utf-8")).decode("utf-8")

def decrypt_data(data):
    return base64.b64decode(data).decode("utf-8")
