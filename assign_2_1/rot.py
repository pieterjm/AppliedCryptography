#!/usr/bin/env python3
# (c) 2020 Frans Schippers, HvA <f.h.schippers@hva.nl>
__version__ = '1.0 2020-11-11'

def rot(txt, nrBytes, nrBits=0):
    """ XOR operates on bytes not strings """
    assert isinstance(txt, bytes)
    assert len(txt)*8 >= (nrBytes*8 + nrBits)

    txtLen = len(txt)
    if txtLen == 0:
        return txt

    # Student work {{

    # from Les 2.1 we have the following formulas
    # right rotate
    # return ((n >> d) | (n << (nBits - d))) & (2**nBits-1)
    # left rotate
    # return ((n << d) | (n >> (nBits - d))) & (2**nBits-1)

    # convert the bytestring to an integer
    n = int.from_bytes(txt,'big')
        
        
    # calculate to total length to shift in bits, bytes are 8 bits
    d = nrBytes * 8 + nrBits

    # nBits is required for the formula form 2.1
    nBits = len(txt) * 8

    # if d > 0, shift right
    if d > 0:
        code = ((n >> d)|(n << (nBits - d))) & ( 2**nBits - 1)

    # if d < 0, shift left, and flip the sign of d
    elif d < 0:
        d = -1 * d
        code = ((n << d) | (n >> (nBits - d))) & (2**nBits-1)

    # if d == 0, no shift is needed
    else:
        code = n

    # convert to code back to bytes
    code = code.to_bytes(txtLen, 'big')    
            
    # Student work }}
    return code

gVbs = False
if __name__ == '__main__':
    import os, sys
    import getopt   
    
    nrBytes = nrBits = 0
    opts, args = getopt.getopt(sys.argv[1:], 'hVB:b:', [ 'bytes=', 'bits=' ])
    for opt, arg in opts:
        if opt == '-V': gVbs = True
        elif opt in [ '-b', '--bits' ]: nrBits = int(arg)
        elif opt in [ '-B', '--bytes' ]: nrBytes = int(arg)

    nrBytes += nrBits // 8
    nrBits = nrBits % 8

    # Maak van alle argumenten een byte-string zonder spaties (0x -> hex-string)
    txt = ''.join(args).replace(' ', '')
    txt = bytes.fromhex(txt[2:]) if txt.startswith('0x') else bytes(txt, 'ascii')

    if gVbs: print('bytes: {}, bits={}'.format(nrBytes, brBits))
    if gVbs: print('txt :', repr(txt))
    try:
        code = rot(txt, nrBytes, nrBits)
    except Exception as e:
        print(e)
        sys.exit()


    if code.isalnum():
        print(code.decode("ascii"))
    else:
        print('0x'+code.hex())

