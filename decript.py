d, n = 525147, 789499

message = str(input("Mensagem: "))
decode_message = ''

for let in message:
    unicode = ord(let)
    m = (unicode ** d % n)
    decode_message += str(chr(m))
print(decode_message)
