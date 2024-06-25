# src/textutils/text_processor.py

import string
from collections import Counter

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        return self.text.translate(translator)

    def word_count(self):
        words = self.text.split()
        return len(words)

    def most_common_words(self, n=10):
        words = self.text.split()
        counter = Counter(words)
        return counter.most_common(n)
