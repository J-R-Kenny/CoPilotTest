import unittest
from AnagramKata import are_anagrams

class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        self.assertEqual(are_anagrams("listen", "silent"), True)
        self.assertEqual(are_anagrams("hello", "world"), False)

# These fail tests are included to demonstrate what a failed test looks like
    def test_anagrams_fail(self):
        self.assertEqual(are_anagrams("python", "typhon"), False)
        self.assertEqual(are_anagrams("cat", "dog"), True)

if __name__ == '__main__':
    unittest.main()