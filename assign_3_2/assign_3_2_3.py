import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

key = "e610ac87daf050aaadf0182660f3f4d2fb46c93739dcb175eb329fc358d208b7"
iv = "bf9526eec98fbf5779d91a85410d9e5d"
encrypted = "ae297723d9c0de5e248a432f22fc70bc1624791fda71c2f197e26ad23348add6"




# aes-256-ctr
cipher = Cipher(
    algorithms.AES(bytes.fromhex(key)),
    modes.CTR(bytes.fromhex(iv)),
    backend=default_backend()
)

decryptor = cipher.decryptor()
decrypted = decryptor.update(bytes.fromhex(encrypted)) + decryptor.finalize()

print(decrypted.decode())

