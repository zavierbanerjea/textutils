# tests/test_text_processor.py

import unittest
from textutils import TextProcessor

class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        self.text = "Hello, world! Hello!"
        self.processor = TextProcessor(self.text)

    def test_remove_punctuation(self):
        self.assertEqual(self.processor.remove_punctuation(), "Hello world Hello")

    def test_word_count(self):
        self.assertEqual(self.processor.word_count(), 3)

    def test_most_common_words(self):
        self.assertEqual(self.processor.most_common_words(), [('Hello,', 1), ('world!', 1), ('Hello!', 1)])

if __name__ == '__main__':
    unittest.main()
