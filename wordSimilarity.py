"""
file: wordSimilarity.py
description: Reads word data from a file and returns the top 5 most similar words to a given word.
language: python3
author: Arnav Gawas
"""

import wordData

def normalizeVectors(word, wordVectors, years):
    """
    Normalize the vector representation of a word based on its count over the years
    Parameters: word (string): The word whose vector is to be normalized
                wordVectors (dictionary): A dictionary where keys are words and values are dictionaries with years as keys and counts as values
                years (list): A list of years to represent the dimensions of the word vector
    Returns: A normalized vector representing the word, or None if the word is not found
    """
    if word not in wordVectors:
        return None
    wordVector = []
    for year in years:
        wordVector.append(wordVectors[word].get(year, 0))
    
    magnitude = 0
    for count in wordVector:
        magnitude += count * count
    if magnitude == 0:
        return wordVector
    magnitude = magnitude ** 0.5
    normalizedVector = []
    for count in wordVector:
        normalizedVector.append(count / magnitude)

    return normalizedVector

def calculateSimilarity(word1, word2, wordVectors, years):
    """
    Calculate the cosine similarity between two words based on their normalized vectors.
    Parameters: word1 (string): The first word for comparison
                word2 (string): The second word for comparison
                wordVectors (dictionary): A dictionary where keys are words and values are dictionaries with years as keys and counts as values
                years (list): A list of years to represent the dimensions of the word vectors
    Returns: The cosine similarity between the two words
    """
    normalizedVector1 = normalizeVectors(word1, wordVectors, years)
    normalizedVector2 = normalizeVectors(word2, wordVectors, years)

    if normalizedVector1 is None or normalizedVector2 is None:
        return 0

    dotProduct = 0
    for i in range(len(normalizedVector1)):
        dotProduct += normalizedVector1[i] * normalizedVector2[i]
    return dotProduct

def topSimilar(words, word):
    """
    Find the top five most similar words to a given word based on cosine similarity
    Parameters: words (dictionary): A dictionary where keys are words and values are dictionaries with years as keys and counts as values
                word (string): The word for which similar words are to be found
    Returns: A list of the top five most similar words to the input word, including the input word itself
    """
    if word not in words:
        return [word]

    years = []
    for counts in words.values():
        for year in counts.keys():
            if year not in years:
                years.append(year)
    years.sort()
    
    wordVectors = {}
    for wordKey in words:
        wordVectors[wordKey] = {}
        for year in years:
            wordVectors[wordKey][year] = words[wordKey].get(year, 0)

    similarities = []
    for word2 in words:
        if word2 == word:
            continue
        similarity = calculateSimilarity(word, word2, wordVectors, years)
        similarities.append((word2, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)

    topSimilarWords = [word]
    for similarWords, _ in similarities[:4]:
        topSimilarWords.append(similarWords)

    return topSimilarWords

if __name__ == "__main__":
    filename = input("Enter word file: ")

    word = input("Enter word: ")

    words = wordData.readWordFile(filename)

    result = topSimilar(words, word)
    print("The most similar words are:", result)
