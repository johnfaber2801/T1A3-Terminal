import pytest
from analyzer import Analysis_text
from analyzer import Word_Frequency
from analyzer import Keyword
from collections import Counter

    
def test_word_frequency():
    text = "This is a sample text for testing word frequency. This text contains word frequency."
    frequency = Word_Frequency(text)
    word_counts = frequency.word_frequency()
    assert word_counts['word'] == 2
    assert word_counts['This'] == 2



