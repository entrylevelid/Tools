# =============================================
#  Text Decryption by Entry Level ID
# =============================================

from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

with open("encrypted_data.txt", "rb") as enc_file:
    cipher_text = enc_file.read()

decrypted_data = cipher_suite.decrypt(cipher_text)
print("Decrypted Text:", decrypted_data.decode())