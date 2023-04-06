def verificar_palindromo(texto):
    texto = texto.lower().replace(" ","")
    return texto == texto [::-1]

texto = "Socoram-me, subi no ônibus em Marrocos"
if verificar_palindromo(texto):
    print(texto, "é um palindromo")
else:
    print(texto, "não é um palindromo")