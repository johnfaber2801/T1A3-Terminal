# from textblob import TextBlob

# class AnalysisText:
#     def __init__(self, text):
#         self.text = text

#     def language_text(self):
#         language = TextBlob(self.text).detect_language()
#         return language

# # Example usage
# text = "This is a sample text."
# analyzer = AnalysisText(text)
# detected_language = analyzer.language_text()
# print(f'Detected language: {detected_language}')

# from langdetect import detect, DetectorFactory
# DetectorFactory.seed = 0
# detect('今一はお前さん')

# print( 'langues is {detect}')

from langdetect import detect

# Open and read the content of the file
file_path = 'src/textexample.txt'
with open(file_path, 'r') as file:
    file_content = file.read()

# Detect the language
detected_language = (detect(file_content)).upper()

print(f'Detected language: {detected_language}')
