from analyzer import Analisis_text
from analyzer import Word_Frequency



file_path= 'src/Englishtext.txt'
# file_path= 'src/spanishtext.txt'
# file_path= 'src/frenchtext.txt'
with open(file_path) as file:
    text = file.read()

#get input text for user
# text_example = text

#instance of Analisis_text class
analizer = Analisis_text(text)
frequency = Word_Frequency(text)

                #FEATURE #1

# Calling methods in Analisis text for feature #1
# word_count = analizer.word_count()
# character_count = analizer.character_count()
# lines_count = analizer.lines_count()
# paragraph_count = analizer.paragraph_count()
# language = analizer.language_text()


# print(f'Number of words are: {word_count}')
# print(f'Number of characters are: {character_count} ')
# print(f'Number of lines are: {lines_count}')
# print(f'Number of paragraphs are: {paragraph_count}')
# print(f'language text: {language}')

                #FEATURE #2

word_frequency = frequency.word_frequency()
print(f' your top 5  most common words are: \n {word_frequency}')