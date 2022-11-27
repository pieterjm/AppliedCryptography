#!/usr/bin/env python3
# (c) 2020 Frans Schippers, HvA <f.h.schippers@hva.nl>
__version__ = '1.0 2020-11-11'

def swap(txt, a, b, l=0):
    """ XOR operates on bytes not strings """
    assert isinstance(txt, bytes)
    # Test de parameters
    assert  0 <= a < len(txt) and 0 <= b < len(txt), "swap: a,b not in range"
    assert  a + l <= len(txt) and b + l <= len(txt), "swap: text to short"
    assert  a == 0 or (a < b and a +l < b) or (b < a and b + l < a), "swap: overlap a+l and b+l"

    # Student work {{
    # the index of the first character in a string is 0
    # the index of the last character in a string is strlen - 1
    # the python substring function is str[start:end:step]
    # start is the first character, end is the last character index, step (if not 1, skips characters)

    # swap b and a if b smaller than a
    if b < a:
        temp = b
        b = a
        a = temp

    # the string basically consists of five parts
    # 1. txt[:a])   The prefix part until the a part
    # 2. txt[a:a+l] The a part with length l to be swapped with b
    # 3. txt[a+l:b] The part between a+l and b
    # 4. txt[b:b+l] The b part with length l to be swapped with a
    # 5. txt[b+l:]  The last part from b+l till the end
    # As a and b are swapped, we create a new byte string in the following order
    #      1.        4.           3.           2.           5.    
    code = txt[:a] + txt[b:b+l] + txt[a+l:b] + txt[a:a+l] + txt[b+l:]
        
    # Student work }}
    return code

gVbs = False
if __name__ == '__main__':
    import os, sys
    import getopt   


    a = b = l = 0
    opts, args = getopt.getopt(sys.argv[1:], 'hVa:b:l:', [])
    for opt, arg in opts:
        if opt == '-V': gVbs = True
        elif opt == '-a': a = int(arg)
        elif opt == '-b': b = int(arg)
        elif opt == '-l': l = int(arg)

    # Maak van alle argumenten een byte-string zonder spaties (0x -> hex-string)
    txt = ''.join(args).replace(' ', '')
    txt = bytes.fromhex(txt[2:]) if txt.startswith('0x') else bytes(txt, 'ascii')

    if gVbs: print('txt :', repr(txt))
    try:
        code = swap(txt, a, b, l)
    except Exception as e:
        print(e)
        sys.exit()

    if code.isalnum():
        print(code.decode("ascii"))
    else:
        print('0x'+code.hex())

