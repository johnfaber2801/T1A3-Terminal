import re
from langdetect import detect

# feature #1 for Basic Text Analysis
class Analisis_text():
    def __init__(self,text):
        self.text = text
       
    def word_count(self): # returns the number of words
        words = (len(re.findall(r'\w+', self.text)))
        return words
    
    def character_count(self): # returns the number of characters
        characters = (len(self.text))
        return characters
    
    def lines_count(self): # returns the number of lines excluding empty lines
        line_count =len([line for line in self.text.splitlines() if line.strip()])#list comphrension
        return line_count
    
    def paragraph_count(self): # returns the number of paragraphs
        paragraphs_count = len([paragraph for paragraph in self.text.split('\n\n') if paragraph.strip()])#list comphrension
        return paragraphs_count
    
    def language_text(self): # returns the language text
        language = (detect(self.text)).upper()
        return language
