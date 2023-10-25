import pytest
from analyzer import Analysis_text
from analyzer import Word_Frequency

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

# test for word count feature
def test_word_count():
    text3 = 'hi hi hi hi hi python python python python python python...'
    count = Analysis_text(text3)
    word_count = count.word_count()
    expected_count = 11
    assert word_count == expected_count

# test for character count
def test_character_count():
    text4 = 'hi hi hi hi hi python python python python python python...'
    count = Analysis_text(text4)
    character_count = count.character_count()
    expected_count = 59
    assert character_count == expected_count

# 2 tests for lines count
def test_lines_count():
     text5 = 'hi hi hi hi hi\n python python python python'
     count = Analysis_text(text5)
     lines_count = count.lines_count()
     expected_count = 2
     assert lines_count == expected_count

     text10 = 'hi hi\n hi hi hi\n python python\n python python'
     count = Analysis_text(text10)
     lines_count = count.lines_count()
     expected_count = 4
     assert lines_count == expected_count

# 2 tests for paragraphs count
def test_paragraph_count():
     text6 = 'hi hi hi hi hi hi\n\n python python python python'
     count = Analysis_text(text6)
     paragraph_count = count.paragraph_count()
     expected_count = 2
     assert paragraph_count == expected_count

     text11 = 'hi hi hi\n\n hi hi hi\n\n python python \n\npython python'
     count = Analysis_text(text11)
     paragraph_count = count.paragraph_count()
     expected_count = 4
     assert paragraph_count == expected_count

# 3 tests in spanish, english and german for language detection feature
def test_language_text():
     text7 = ' good morning sydney, how is things going? i hope all is good'
     language = Analysis_text(text7)
     language_result = language.language_text()
     expected_language = 'EN'
     assert language_result == expected_language

     text8 = ' buenos dias sydney como estan? espero todo este muy bien'
     language = Analysis_text(text8)
     language_result = language.language_text()
     expected_language = 'ES'
     assert language_result == expected_language

     text9 = "Guten Morgen Sydney, wie geht's? Ich hoffe, alles ist gut"
     language = Analysis_text(text9)
     language_result = language.language_text()
     expected_language = 'DE'
     assert language_result == expected_language



    
   

