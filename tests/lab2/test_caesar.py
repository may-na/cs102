import unittest 
import sys
sys.path.append('../../src/lab2')

from caesar import encrypt_caesar, decrypt_caesar

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar("PYTHON"), 'SBWKRQ')
        self.assertEqual(encrypt_caesar("python"), 'sbwkrq')
        self.assertEqual(encrypt_caesar("Python3.6"), 'Sbwkrq3.6')
        self.assertEqual(encrypt_caesar(""), '')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), 'PYTHON')
        self.assertEqual(decrypt_caesar("sbwkrq"), 'python')
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), 'Python3.6')
        self.assertEqual(decrypt_caesar(""), '')

if __name__ == '__main__':
    unittest.main()
