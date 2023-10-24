from analyzer import Analysis_text
from analyzer import Word_Frequency
from analyzer import Keyword


def read_file(file_path):
     try:        
        with open(file_path) as file:
         return file.read()
    
     except Exception as e:
        print(f"Error: {e}")

        # Feature #1
def analyze_text(analyzer):
    analyzer.word_count()
    analyzer.character_count()
    analyzer.lines_count()
    analyzer.paragraph_count()
    analyzer.language_text()

def main():
                #file path must be specified here
    file_path = 'src/enter_your_text_here.txt'
    file_text = read_file(file_path)

    if file_text:

        analyzer = Analysis_text(file_text)
        frequency = Word_Frequency(file_text)
        keywords = Keyword(file_text)
                
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

            try:
                if choice == '1': 
                    analyze_text(analyzer)

                elif choice == '2':
                    frequency.word_frequency()

                elif choice == '3':
                    keywords.keyword_extraction()
                
                elif choice == '4':
                    print('--------------------------------')
                    print('Thanks for using Text File Analizer! ')
                    print('--------------------------------')
                    break
                else:
                    raise ValueError('Invalid choice, Input must be number 1, 2, 3 or 4.\nPlease try again!')
                              
                while True:
                     continue_option = input('Would you like to continue? (yes/no): ').lower()
                     if continue_option in ['yes', 'no']:
                        break                       
                     else:
                        print("Invalid choice, Input must be 'yes' or 'no'")    

                if continue_option != 'yes':
                    print('--------------------------------')
                    print('Thanks for using Text File Analyzer!')
                    print('--------------------------------')
                    break     
                       
            except Exception as e:
             print(f"Error: {e}")
            
if __name__ == "__main__":
    main()