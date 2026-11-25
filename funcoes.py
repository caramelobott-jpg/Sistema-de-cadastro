def regularizado_nome(nome):
    if nome == "nome":
        print("Nome quardado")
        return
    
def iregular_idade(idade):
    if idade >= 18:
        print("voce e maior de idade")
    else:
        print("Voce e menor de 18")
    return

def regular_email(emaill):
    if "@gmail.com" in  emaill:
        print("Gmail Valido!")
    else:
        print("Gmail invalido")
    return emaill



def salvacadastro(nome, idade, gmail):

    cadastro = {
        "nome": nome,
        "idade": idade,
        "Gmail": gmail
    }

    print(cadastro)