import random
import string

def gerear_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = '' .join(random.choice(caracteres) for i in range (tamanho))
    return senha

senha = gerear_senha()
print("A senha gerada é: ", senha)