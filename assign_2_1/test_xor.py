#!/usr/bin/env python3
# (c) 2020 Frans Schippers, HvA <f.h.schippers@hva.nl>
__version__ = '1.0 2020-11-15'

import unittest
import xor

class TestFindTld(unittest.TestCase):


    def test01(self):
        key = bytes.fromhex('13171d171f170d17171f131d13')
        code = bytes('trurvzorevpug', encoding='ascii')
        refText = b'geheimbericht'
        text = xor.xor(code, key)
        self.assertEqual(text, refText)
        

    def test02(self):
        key = bytes.fromhex('171d191e131d0a1d0802071406')
        code = bytes('trurvzorevpug', encoding='ascii')
        refText = b'collegeomtwaa'
        text = xor.xor(code, key)
        self.assertEqual(text, refText)


    def test03(self):
        key = bytes.fromhex('151c0c06130206050c1a1c1108')
        code = bytes('trurvzorevpug', encoding='ascii')
        refText = b'anytexiwilldo'
        text = xor.xor(code, key)
        self.assertEqual(text, refText)


if __name__ == '__main__':
    unittest.main()
