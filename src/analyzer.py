import re


class Analisis_text():
    def __init__(self,text):
        self.text = text
       
    def word_count(self):
        words = (len(re.findall(r'\w+', self.text)))
        return words