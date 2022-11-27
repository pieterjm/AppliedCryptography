#!/usr/bin/env python3
# (c) 2020 Frans Schippers, HvA <f.h.schippers@hva.nl>
__version__ = '1.9 2020-11-11'

def xor(txt, key):
    """ XOR operates on bytes not strings """
    assert isinstance(txt, bytes)
    assert isinstance(key, bytes)
    # lengte checken, is assert is equal length
    assert len(txt) == len(key)
    
    code = b''

    # itereer over characters/bytes
    for i in range(len(txt)):
        # xor per byte    
        # voeg toe aan resultaat: code
        code += bytes(chr(txt[i] ^ key[i]), 'ascii')
        
        
    return code

gVbs = False
if __name__ == '__main__':
    import os, sys
    import getopt   

    key = ''
    opts, args = getopt.getopt(sys.argv[1:], 'hVk:', [ 'key=' ])
    for opt, arg in opts:
        if opt == '-V': gVbs = True
        elif opt == '-k' or opt == '--key': key = arg

    # Convert key naar bytes (0x geeft aan dat het een hex-string is
    key = bytes.fromhex(key[2:]) if key.startswith('0x') else bytes(key, 'ascii')
    # Maak van alle argumenten een byte-string zonder spaties (0x -> hex-string)
    txt = ''.join(args).replace(' ', '')
    txt = bytes.fromhex(txt[2:]) if txt.startswith('0x') else bytes(txt, 'ascii')

    if gVbs:
        print('key :', repr(key))
        print('key :', '0x'+key.hex(), len(key))
    if gVbs:
        print('txt :', repr(txt))
        print('txt :', '0x'+txt.hex(), len(txt))
    code = xor(txt, key)

    if code.isalnum():
        print(code.decode("ascii"))
        if gVbs: print('0x'+code.hex(), len(code))
    else:
        print('0x'+code.hex())

