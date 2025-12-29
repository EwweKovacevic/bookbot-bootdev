from stats import countWords
from stats import countLetters
from stats import finalReport
from stats import get_book_text
import sys
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return


    text = get_book_text(sys.argv[1])
    wordCount = countWords(text)
    letters = countLetters(text)
    # print(f"Found {wordCount} total words")
    # print(letters)
    print(finalReport(sys.argv[1]))
    return

main()