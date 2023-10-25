import unittest
import sys
sys.path.append('../../src/lab2')
from rsa import is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt

class TestRSAFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(8))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_generate_keypair(self):
        p, q = 11, 19
        public_key, private_key = generate_keypair(p, q)

    # Проверка на то, что оба ключа имеют два элемента
        self.assertEqual(len(public_key), 2)
        self.assertEqual(len(private_key), 2)

    # Проверка, что оба ключа содержат только целые числа
        self.assertIsInstance(public_key[0], int)
        self.assertIsInstance(public_key[1], int)
        self.assertIsInstance(private_key[0], int)
        self.assertIsInstance(private_key[1], int)


if __name__ == '__main__':
    unittest.main()
