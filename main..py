
import funcoes
print("Banco elevoler")

print("Cadastro Oficial")

dados_nome = input("Digite seu nome:").lower()
dados_idade = int(input("Digite sua idade:"))
dados_gmail = input("Digite seu gmail:").lower()

    

import json

def salvacadastro(dados_nome, dados_idade, dados_gmail):
    caminho_arquivo = "cadastros.json"

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            cadastros = json.load(arquivo)
    except FileNotFoundError:
        cadastros = []

    novo_usuario = {
        "nome": dados_nome,
        "idade": int(dados_idade),
        "gmail": dados_gmail,
    }

    cadastros.append(novo_usuario)

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)








if len(dados_nome) >= 3:
    print("Verificação valida")
    if int(dados_idade) >= 18:
        print("idade valida")
        if len(dados_gmail) >= 10 and "@gmail.com" in dados_gmail:
            print("Gmail valido")
            salvacadastro(dados_nome, dados_idade, dados_gmail)
        else:
            print("Gmail invalido")
    else:
        print("idade invalida")
else:
    print("Nome invalido")

