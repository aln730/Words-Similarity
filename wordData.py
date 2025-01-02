""" 
file: wordData.py
description: Reads a word file and calculates total occurrences by year.
language: python3
author: Arnav Gawas
"""

def readWordFile(fileName):
    """
    Reads a file and returns a dictionary of words and their yearly counts.
    Parameters: fileName (string): Name of the file to read.
    Returns: A dictioary where keys are words and values are dictionaries with year as keys and occurances as values.
    """

    fullPath = "data/" + fileName
    words = {}

    with open(fullPath, 'r') as file:
        currWord = None 
        counts = {}

        for line in file:
            line = line.strip()
            if ',' in line:  
                year, count = line.split(',')
                counts[int(year)] = int(count)
            else: 
                if currWord:
                    words[currWord] = counts
                currWord = line
                counts = {} 
        if currWord:
            words[currWord] = counts
            
    return words

def totalOccurrences(word, words):
    """
    Computes the total occurrences of a word in the data.
    Parameters:word (string): The word to search for.
               words (dictionary): dictioary where keys are words and values are dictionaries with year as keys and occurances as values.
    Returns:Total occurrences of the word, or 0 if not found.
    """
    if word not in words:
        return 0
    
    yearCounts = words[word]

    totalCounts = sum(yearCounts.values())

    return totalCounts

if __name__ == "__main__":
    file_name = input("Enter word file: ")
    
    words = readWordFile(file_name)
    
    word = input("Enter word: ")

    total = totalOccurrences(word, words)
    print("Total occurrences of", word," : ", total)

    print(words)