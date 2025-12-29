def get_book_text(file):
    with open(file) as f:
        string = f.read()
    return(string)

def countWords(string):
    words = string.split()
    wordCount = len(words)
    return wordCount

def countLetters(string):
    letters = {}
    lowerAll = string.lower()
    for char in lowerAll:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

def finalReport(file):
    text = get_book_text(file)
    filePath = file
    wordCount = countWords(text)
    letters = countLetters(text)
    sortByNumber = sorted(letters.items(), key=lambda x: x[1], reverse=True)

    char_report = ""
    for char, count in sortByNumber:
        char_report += f"{char}: {count}\n"

    report = f"============ BOOKBOT ============ \nAnalyzing book found at: {filePath} \n----------- Word Count ---------- \nFound {wordCount} total words \n--------- Character Count ------- \n{char_report} \n============= END ==============="
    return report