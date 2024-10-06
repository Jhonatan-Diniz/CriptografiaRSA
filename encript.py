print("Insira os valores da chave separados por um espaço exemplo ->  e n")

e, n = input("Chave Pública -> ").split(" ")
chave = (int(e), int(n))
msg = input("Mensagem -> ")
