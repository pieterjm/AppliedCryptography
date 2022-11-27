#!/usr/bin/env python3
# (c) Applied Cryptography 2021b2 f.h.schippers@hva.nl (2020)
__version__ = '1.0 2020-11-21'

from cryptography.hazmat.primitives import hashes

def normalize(text: bytes) -> bytes:
    """ De text (bytes wordt genormaliseerd
        o.a. door het verwijderen van newlines
    """

    # Student work {{
    text = text.lower()
    text = text.replace(b'\n', b'')
    text = text.replace(b'\r', b'')
    text = text.replace(b',', b'')
    text = text.replace(b';', b'')
    text = text.replace(b'.', b'')
    text = text.replace(b':', b'')
    text = text.replace(b' ', b'')

    # you can dump the text to spot differences. Text3 also contains different wording (ick instead of ik)
    # print(text)

    # Student work }}

    return text # Dit moet dus beter worden, nu is het geen normalisatie


def sha256hex(fname: str) -> str:
    """ De SHA256 van de inhoud van de file met naam `fname` wordt berekend.
        Het resultaat is de hex-representatie van hash.
    """

# Student work {{
    # The process to do this in python is explained in lesson 3.1    
    digest = hashes.Hash(hashes.SHA256())

    # Open the filename in binary mode (read = r, binary = b)
    with open(fname,"rb") as file:
        # add data to the file
        digest.update(normalize(file.read()))

    # complete digesting
    digestBytes = digest.finalize()

    # convert to Hex
    digestHex = digestBytes.hex()
    
# Student work }}

    return digestHex

if __name__ == '__main__':
    digestHexRef = sha256hex('wilhelmus1.txt')
    for fname in [ 'wilhelmus2.txt', 'wilhelmus3.txt' ]:
        digestHex = sha256hex(fname)
        print('Sha256:  {}: {} '.format(fname, digestHex), end='')
        if digestHex == digestHexRef:
            print(' Correct', end='')
        else:
            print(' Different: {}'.format(digestHexRef), end='')
        print()
