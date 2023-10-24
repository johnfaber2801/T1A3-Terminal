import pytest
from analyzer import Analysis_text
from analyzer import Word_Frequency
from analyzer import Keyword
from collections import Counter

                        # Feature #2

    #test word frequency analysis feature
def test_word_frequency():
    text = "This is a sample text for testing word frequency. This text contains word frequency."
    frequency = Word_Frequency(text)
    word_counts = frequency.word_frequency()
    assert word_counts['word'] == 2
    assert word_counts['This'] == 2

# error test when the file does not contain text
def test_word_frequency_empty_text():
    try:
        empty_text = ""
        word_frequency_instance = Word_Frequency(empty_text)
        result = word_frequency_instance.word_frequency()
        assert result == {}
    except Exception as e:
            print(f"Error: {e}")


                            # Feature #1

def test_word_count():
    text3 = 'hi hi hi hi hi python python python python python python...'
    count = Analysis_text(text3)
    word_count = count.word_count()
    expected_count = 11
    assert word_count == expected_count

    
   

