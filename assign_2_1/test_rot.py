#!/usr/bin/env python3
# (c) 2020 Frans Schippers, HvA <f.h.schippers@hva.nl>
__version__ = '1.0 2020-11-15'

import unittest
import rot

class TestFindTld(unittest.TestCase):


    def test01(self):
        text =b'abcdefghij'
        code = rot.rot(text, 0)
        refCode = b'abcdefghij'
        self.assertEqual(code, refCode)
        

    def test02(self):
        text = b'abcdefghij'
        code = rot.rot(text, 4)
        refCode = b'ghijabcdef'
        self.assertEqual(code, refCode)


    def test03(self):
        text = b'abcdefghij'
        code = rot.rot(text, -4)
        refCode = b'efghijabcd'
        self.assertEqual(code, refCode)


if __name__ == '__main__':
    unittest.main()
