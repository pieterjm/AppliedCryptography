import os

# 1. ik versleutel de text in python
# 2. decoderen met system command
# 3. versleutelen met system command
# 4. decoderen met python

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


plaintext = b'Dit is tekst om te encrypten'
key = "57dfae4dfcacab86e6e47af41e8e1072"
iv = "12090a5fe972324b7d6ede2e81631e19"


cipher = Cipher(
    algorithms.AES(bytes.fromhex(key)),
    modes.CBC(bytes.fromhex(iv)),
    backend=default_backend()
)

# voeg padding toe
padder = padding.PKCS7(128).padder()
padded = padder.update(plaintext)
padded += padder.finalize()

encryptor = cipher.encryptor()
encoded = encryptor.update(padded) + encryptor.finalize()
print("Versleuteld (hex): {} ".format(encoded.hex()))

# schrijf weg naar file
with open("encrypted.dat","wb") as file:
    file.write(encoded)

# Decoderen op de command line
print("Decoding op de command line geeft:")
os.system("openssl aes-128-cbc -d -K {key} -iv {iv} -out - -in encrypted.dat".format(key=key,iv=iv))
print("")

# Encoding op de command line
print("Encoding op de command line:")
with open("plaintext.txt","wb") as file:
    file.write(plaintext)
os.system("openssl aes-128-cbc -e -K {key} -iv {iv} -in plaintext.txt -out encrypted.dat".format(key=key,iv=iv))

print("Decrypten met python")
with open("encrypted.dat","rb") as file:
    data = file.read()

    decryptor = cipher.decryptor()
    decrypted = decryptor.update(data) + decryptor.finalize()
    
    unpadder = padding.PKCS7(128).unpadder()
    unpadded = unpadder.update(decrypted)
    unpadded += unpadder.finalize()

    print(unpadded.decode())
