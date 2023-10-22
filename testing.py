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

from rake_nltk import Rake
from langdetect import detect

def extract_keywords(text):
    detected_language = detect(text)
    
    # Map detected language to Rake language code (if needed)
    language_mapping = {
        'en': 'english',  # English
        'es': 'spanish'   # Spanish
        # Add more language codes and corresponding Rake language codes as needed
    }
    
    # Set Rake language based on detected language (default to English if not detected)
    rake_language = language_mapping.get(detected_language, 'english')
    
    rake_nltk_var = Rake(language=rake_language)
    rake_nltk_var.extract_keywords_from_text(text)
    keywords_extracted = rake_nltk_var.get_ranked_phrases()
    return keywords_extracted

# Example usage
input_text = 'En muchas ocasiones el campo de actuación del aprendizaje automático se solapa con el de la estadística inferencial'
keywords = extract_keywords(input_text)

print("Extracted Keywords:")
print(keywords)


