import hashlib

mensagem = "teste123"

# SHA256
hash_sha256 = hashlib.sha256(mensagem.encode()).hexdigest()
print("SHA256:", hash_sha256)

# MD5 (menos seguro)
hash_md5 = hashlib.md5(mensagem.encode()).hexdigest()
print("MD5:", hash_md5)
