from analyzer import Analisis_text

file_path= 'src/textexample.txt'
with open(file_path) as file:
    text = file.read()

#get input text for user
# text_example = text

#instance of Analisis_text class
analizer = Analisis_text(text)

# Call word_count method and print the result
word_count = analizer.word_count()
print(f'Number of words in the text: {word_count}')