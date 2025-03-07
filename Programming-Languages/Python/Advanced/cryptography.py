from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = "Secret Data"
encrypted = cipher.encrypt(message.encode())
decrypted = cipher.decrypt(encrypted).decode()

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
