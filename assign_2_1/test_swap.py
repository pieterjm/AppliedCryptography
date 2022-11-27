#!/usr/bin/env python3
# (c) 2020 Frans Schippers, HvA <f.h.schippers@hva.nl>
__version__ = '1.0 2020-11-15'

import unittest
import swap

class TestFindTld(unittest.TestCase):

    def test00(self):
        text =b'abcdefghij'
        code = swap.swap(text, 2, 6, 0)
        refCode = b'abcdefghij'
        self.assertEqual(code, refCode)


    def test01(self):
        text =b'abcdefghij'
        code = swap.swap(text, 2, 6, 2)
        refCode = b'abghefcdij'
        self.assertEqual(code, refCode)

    def test02(self):
        text =b'abcdefghij'
        code = swap.swap(text, 6, 2, 2)
        refCode = b'abghefcdij'
        self.assertEqual(code, refCode)

    def test03(self):
        text =b'abcdefghij'
        code = swap.swap(text, 0, 5, 5)
        refCode = b'fghijabcde'
        self.assertEqual(code, refCode)




if __name__ == '__main__':
    unittest.main()
