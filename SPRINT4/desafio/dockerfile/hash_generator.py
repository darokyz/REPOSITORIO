import hashlib

data = input("Digite uma string para gerar o hash: ")

# opa gerando o hash SHA-1
hash_result = hashlib.sha1(data.encode())

print("Hash SHA-1 gerado:", hash_result.hexdigest())
