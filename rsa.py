import random
import math


# Encontra o maximo divisor comum entre dois números
def mdc(a: int, b: int) -> int:
    resto: int = 0
    while True:
        resto = a % b
        if (resto == 0):
            break
        a = b
        b = resto
    return b


# Checa se um número é primo
def e_primo(num) -> bool:
    if (num == 1 or num % 2 == 0):
        return False

    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if (num % i == 0):
            return False
    return True


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
    # 1 < e < tot e mdc(e, tot) = 1

    e: int = random.randint(2, tot-1)
    # checa se o mdc entre o totiente e o valor de e são co-primos
    while mdc(tot, e) != 1:
        e = random.randint(2, tot-1)

    # encontrando o numero 'd' que representa a primeira parte da private key |
    # 'd' precisa ser um valor que torne | d*e mod tot = 1 | verdadeiro

    d: int = 1
    while (True):
        if ((e * d) % tot == 1 and d != e):
            break
        d += 1

    return (e, n), (d, n)


while True:
    print("\nG -> Gerar chaves\nC -> Criptografia\nD -> Descriptografia\nS -> Sair")

    opt: str = input("> ").upper()

    while opt not in "GCD":
        print("Digite um valor válido")
        print("\nG -> Gerar chaves\nC -> Criptografia\nD -> Descriptografia\nS -> Sair")
        opt = input("> ").upper()

    # Opção de gerar cheves
    if (opt == 'G'):
        chave_publica, chave_privada = gerando_chaves()

        print(f"Chave pública: {chave_publica}")
        print(f"Chabe privada: {chave_privada}")

    # Opção de criptografar mensagem
    elif (opt == 'C'):
        message: str = input("Mensagem: ")
        chave = input("Chave Pública -> ").split(" ")
        e, n = int(chave[0]), int(chave[1])

        criptography: str = ''

        for char in message:
            encode: int = ord(char)
            c: str = str(pow(encode, e, n))
            criptography += c + ' '

        print(f"Texto criptografado: {criptography}")

    # Opção de Descriptografar mensagem
    elif (opt == 'D'):
        message: str = input("Mensagem: ")
        chave = input("Chave Privada: ").split(" ")
        d, n = int(chave[0]), int(chave[1])

        descriptography: str = ''

        for char in message:
            d = pow(int(char), d, n)
            decode = chr(d)
            descriptography += decode

        print(descriptography)

    # Sair do programa
    elif (opt == 'S'):
        print("Saindo...")
        break
