#!/usr/bin/env python3
# (c) Applied Cryptography 2021b2 f.h.schippers@hva.nl (2020)
__version__ = '1.0 2020-11-21'

from cryptography.hazmat.primitives import hashes

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
        digest.update(file.read())

    # complete digesting
    digestBytes = digest.finalize()

    # convert to Hex
    digestHex = digestBytes.hex()
    
    # Student work }}

    return digestHex

gChecks = {
    'wilhelmus1.txt': "5e0a9cb2f5a5eff43cfcf86807e65209da6951bc940ef300f234348356eed778",
    'wilhelmus2.txt': "9e96a8c0eea54855a82fe65f6e6bc18d318079a17066a38c5ec9c2e2e1c41ba5",
    'wilhelmus3.txt': "9e5a685b81688694de9a43478bae4c56832a609eaed1fd7f988f6fa8922c505f",
}


if __name__ == '__main__':
    for fname in [ 'wilhelmus1.txt', 'wilhelmus2.txt', 'wilhelmus3.txt' ]:
        digestHex = sha256hex(fname)
        print('Sha256:  {}: {} '.format(fname, digestHex), end='')
        if fname in gChecks:
            if digestHex == gChecks[fname]:
                print(' Correct', end='')
            else:
                print(' Different: {}'.format(gChecks[fname]), end='')
        print()
