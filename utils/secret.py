import random
import string


# Gerar uma chave secreta aleatória
def gerar_chave_secreta(tamanho=24):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))
