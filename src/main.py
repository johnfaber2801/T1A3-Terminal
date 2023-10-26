from analyzer import Analysis_text
from analyzer import Word_Frequency
from analyzer import Keyword


def analyze_text(analyzer):  # Feature #1
    analyzer.word_count()
    analyzer.character_count()
    analyzer.lines_count()
    analyzer.paragraph_count()
    analyzer.language_text()


def get_user_input():  # input text from user
    while True:
        try:
            user_text = input('Enter the text you want to analyze:\n\n ')
            if len(user_text.strip()) == 0:
                raise ValueError('Input cannot be empty. Please enter text')
            return user_text
        except Exception as e:
            print(f"Error: {e}")


def main():
    print('----------------------------')
    print('Welcome to Text File Analyzer')
    print('----------------------------')
    user_text = get_user_input()

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
                raise ValueError('Invalid choice, Input must be 1,2,3 or 4.')
            while True:
                option = input('\nWould you like to continue? yes/no ').lower()
                if option in ['yes', 'no']:
                    break
                else:
                    print("\nInvalid choice, Input must be 'yes' or 'no'")
            if option != 'yes':
                print('--------------------------------')
                print('Thanks for using Text File Analyzer!')
                print('--------------------------------')
                break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
