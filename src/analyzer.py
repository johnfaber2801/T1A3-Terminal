import re
from langdetect import detect
from collections import Counter
from rake_nltk import Rake
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# feature #1 for Basic Text Analysis
class Analysis_text():
    def __init__(self,text):
        self.text = text
       
    def word_count(self): # returns the number of words
        words = (len(re.findall(r'\w+', self.text)))
        print(f'Number of words are: {words}')
           
    def character_count(self): # returns the number of characters
        characters = (len(self.text))
        print(f'Number of characters are: {characters} ')
       
    def lines_count(self): # returns the number of lines excluding empty lines
        line_count =len([line for line in self.text.splitlines() if line.strip()])#list comphrension
        print(f'Number of lines are: {line_count}')
          
    def paragraph_count(self): # returns the number of paragraphs
        paragraphs_count = len([paragraph for paragraph in self.text.split('\n\n') if paragraph.strip()])#list comphrension
        print(f'Number of paragraphs are: {paragraphs_count}')
    
    def language_text(self): # returns the language text
        language = (detect(self.text)).upper()
        print(f'language text: {language}')

# feature #2 Word frequency analysis

class Word_Frequency():
    def __init__(self,text):
        self.text = text

    def  word_frequency(self): #will return top 5 most common words
        frequency= dict(Counter(self.text.split()).most_common(5))
        print(f' your top 5  most common words are: \n {frequency}')

        return frequency
    
# feature #3 keyword extraction

class Keyword():
    def __init__(self,text):
        self.text = text

    def keyword_extraction(self):
        language = (detect(self.text))
        language_list = {'en': 'english', 'es': 'spanish', 'fr': 'french', 'it': 'italian'}
        rake_language = language_list.get(language,'english') # 'Get' used to extract from dictionaries
        rake_nltk_var = Rake(language=rake_language)
        rake_nltk_var.extract_keywords_from_text(self.text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()[:5]
        print (f' The Top 5 keywords of your text are: \n {keyword_extracted}')
       
      

    