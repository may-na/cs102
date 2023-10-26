import unittest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class TestVigenereEncryptionDecryption(unittest.TestCase):
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("HELLO", "A"), 'HELLO')
        self.assertEqual(encrypt_vigenere("hello", "a"), 'hello')
        self.assertEqual(encrypt_vigenere("HELLO", "HI"), 'OMSTV')

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("HELLO", "A"), 'HELLO')
        self.assertEqual(decrypt_vigenere("hello", "a"), 'hello')
        self.assertEqual(decrypt_vigenere("OMSTV", "HI"), 'HELLO')

if __name__ == '__main__':
    unittest.main()
