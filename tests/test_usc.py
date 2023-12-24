import unittest
import random

from src.usc import UniShiftCipher
class TestUniShiftCipher(unittest.TestCase):
    def testNotEqual(self):
        cipher = UniShiftCipher().encrypt
        text = "abc"
        shift = random.randrange(1, 27, 1)
        self.assertNotEqual(cipher(text, shift), text)

    def testErrorOnWrongShiftValue(self):
        cipher = UniShiftCipher()
        text = "abc"
        shift = "a"
        with self.assertRaises(ValueError):
            cipher.encrypt(text, shift)

    def testErrorOnWrongShiftRange(self):
        cipher = UniShiftCipher()
        text = "abc"
        shift = 500
        with self.assertRaises(Exception):
            cipher.encrypt(text, shift)
