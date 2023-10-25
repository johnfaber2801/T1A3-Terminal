from analyzer import Analysis_text
from analyzer import Word_Frequency
from analyzer import Keyword

        # Feature #1
def analyze_text(analyzer):
    analyzer.word_count()
    analyzer.character_count()
    analyzer.lines_count()
    analyzer.paragraph_count()
    analyzer.language_text()

def main():
    print('--------------------------------')
    print('Welcome to Text File Analyzer')
    print('--------------------------------')
   
    user_text = input('Enter the text you want to analyze:\n\n ')         

    while True:    
            
            analyzer = Analysis_text(user_text)
            frequency = Word_Frequency(user_text)
            keywords = Keyword(user_text)

            print('\nChoose an option for you text\n')
            print('1. Text Analysis')
            print('2. Word Frequency Analysis')
            print('3. Keywords extraction')
            print('4. Exit')

            choice = input('\nEnter choice:  ')

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