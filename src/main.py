from analyzer import Analisis_text
from analyzer import Word_Frequency
from analyzer import Keyword

file_path= 'src/enter_your_text_here.txt'
with open(file_path) as file:
    file_text = file.read()

analyzer = Analisis_text(file_text)
frequency = Word_Frequency(file_text)
keywords = Keyword(file_text)

        # Choice #1
def analyze_text(analyzer):
    analyzer.word_count()
    analyzer.character_count()
    analyzer.lines_count()
    analyzer.paragraph_count()
    analyzer.language_text()

print('--------------------------------')
print('Welcome to Text File Analyzer')
print('--------------------------------')

while True:    
    
        print('Choose an option')
        print('1. Text Analysis')
        print('2. Word Frequency Analysis')
        print('3. Keywords extraction')
        print('4. Exit')

        choice = input('Enter choice:  ')

        if choice == '1': 
            analyze_text(analyzer)

        elif choice == '2':
            word_frequency = frequency.word_frequency()

        elif choice == '3':
            keywords_extracted = keywords.keyword_extraction()
        
        elif choice == '4':
            print('Thanks for using Text File Analizer! ')
            break

        else: 
            print('--------------------------------')
            print('Invalid choice, Please try again')
            print('--------------------------------')

        while True:
            continue_option = input('Would you like to continue? (yes/no): ').lower()
            if continue_option in ['yes', 'no']:
                break
            else:
                print('Invalid input. Please enter "yes" or "no".')

        if continue_option != 'yes':
            print('--------------------------------')
            print('Thanks for using Text File Analizer! ')
            print('--------------------------------')
            break
