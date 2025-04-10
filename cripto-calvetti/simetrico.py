from cryptography.fernet import Fernet

# Gerar uma chave simétrica
chave = Fernet.generate_key()
cipher = Fernet(chave)

# Mostrar a chave (opcional)
print("🔑 Chave gerada:", chave.decode())

# Texto original
mensagem_original = "Vai Corinthians"

# Criptografar a mensagem
mensagem_criptografada = cipher.encrypt(mensagem_original.encode())

# Descriptografar a mensagem
mensagem_descriptografada = cipher.decrypt(mensagem_criptografada).decode()

# Exibir resultados

print("\nMensagem Criptografada:")
print(mensagem_criptografada.decode())

print("\nMensagem Descriptografada:")
print(mensagem_descriptografada)
