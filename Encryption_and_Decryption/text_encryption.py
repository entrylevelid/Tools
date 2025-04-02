from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

cipher_suite = Fernet(key)

plaintext = input("Enter the text to encrypt: ").encode()

cipher_text = cipher_suite.encrypt(plaintext)
print("Encrypted Text:", cipher_text)

with open("encrypted_data.txt", "wb") as enc_file:
    enc_file.write(cipher_text)

print("Data has been encrypted and saved to 'encrypted_data.txt' ")