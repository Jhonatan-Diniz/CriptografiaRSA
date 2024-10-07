import random
import math


# Encontra o máximo divisor comum entre dois números usando o algoritmo
# Euclidiano Estendido
def emdc(a: int, b: int) -> tuple:
    # Quando o resto for zero o código volta
    if a == 0:
        return (b, 0, 1)

    # Usando a recursividade para descobrir o mdc e os coeficientes de a e b
    m, y, x = emdc(b % a, a)
    # Retorna o mdc, o coeficiente de a e o coeficiente de b
    return (m, x - (b//a) * y, y)


# Checa se um número é primo
def e_primo(num) -> bool:
    if (num == 1 or num % 2 == 0):
        return False

    # Percorre todos os números ímpares até a raiz de num, se houve algum
    # divisor então num não é primo
    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if (num % i == 0):
            return False
    return True


# Define o módulo multiplicativo
def modInverso(a, b) -> int:
    # Pegando o mdc e os coeficientes de a e b, porém o coeficiente y não é
    # importante
    mdc, x, _ = emdc(a, b)
    if mdc != 1:
        print("Não há modulo!")
        return 0

    # Retorna o módulo do coeficiente de a por b
    return x % b


# Gera um número aleatório ate que seja primo
def gerando_primos(minimo: int, maximo: int) -> int:
    primo = random.randint(minimo, maximo)
    # checa se um numero é primo se não for gera outro número e retorna à
    # verificação
    while (not e_primo(primo)):
        primo = random.randint(minimo, maximo)
    return primo


# gerando as chaves
def gerando_chaves() -> tuple:
    # gera dois números diferentes
    p, q = gerando_primos(1000, 10000), gerando_primos(1000, 10000)
    p, q = gerando_primos(1000, 10000), gerando_primos(1000, 10000)

    while p == q:
        p, q = gerando_primos(1000, 10000), gerando_primos(1000, 10000)

    # produto dos numeros primos
    n: int = p * q

    # totiente de n
    tot: int = (p-1)*(q-1)

    # escolhendo um numero 'e' que representa a primeira parte da public key |
    # 1 < e < tot e emdc(e, tot) = 1

    e: int = random.randint(2, tot-1)
    # checa se o emdc entre o totiente e o valor de e são co-primos
    while emdc(tot, e)[0] != 1:
        e = random.randint(2, tot-1)

    # encontrando o numero 'd' que representa a primeira parte da private key |
    # 'd' precisa ser um valor que torne | d*e mod tot = 1 | verdadeiro

    # Módulo inverso de e por tot
    d: int = modInverso(e, tot)

    # Retorna os valores das chaves públicas e privadas
    return (e, n), (d, n)


while True:
    print("\nG -> Gerar chaves\nC -> Criptografia\nD -> Descriptografia\nS -> Sair")

    opt: str = input("> ").upper()

    while opt not in "GCDS":
        print("Digite um valor válido")
        print("\nG -> Gerar chaves\nC -> Criptografia\nD -> Descriptografia\nS -> Sair")
        opt = input("> ").upper()

    # Opção de gerar cheves
    if (opt == 'G'):
        chave_publica, chave_privada = gerando_chaves()

        print(f"Chave pública:\n {chave_publica[0]} {chave_publica[1]}\n")
        print(f"Chabe privada:\n {chave_privada[0]} {chave_privada[1]}\n")

    # Opção de criptografar mensagem
    elif (opt == 'C'):
        message: str | list = input("Mensagem: ")
        chave = input("Chave Pública -> ").split(" ")
        e, n = int(chave[0]), int(chave[1])

        criptography: str = ''

        for char in message:
            encode: int = ord(char)
            c: str = str(pow(encode, e, n))
            criptography += c + ' '

        print(f"Texto criptografado:\n{criptography}\n")

    # Opção de Descriptografar mensagem
    elif (opt == 'D'):
        message: str | list = input("Mensagem: ").split(' ')
        chave = input("Chave Privada: ").split(" ")
        d, n = int(chave[0]), int(chave[1])

        descriptografado: str = ''

        for char in message:
            ch = pow(int(char), d, n)
            decode = chr(ch)
            descriptografado += decode

        print(f"Texto descriptografado:\n{descriptografado}\n")

    # Sair do programa
    elif (opt == 'S'):
        print("Saindo...")
        break
