import unittest
from wb import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("MatriX"), 2)

if __name__ == '__main__':
    unittest.main()