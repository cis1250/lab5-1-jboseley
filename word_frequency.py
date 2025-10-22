#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True
    
# To get and validate the sentence input.
def get_sentence():
    user_sentence = input("Enter a sentence: ")
    while(is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
    return user_sentence

# To calculate word frequencies.
def calculate_frequencies(sentence):
    sentence = sentence.lower()
    for char in ".,?!:;'\"(){}[]":
        sentence = sentence.replace(char, "")
    words = user_sentence.split()
    unique_words = []
    frequencies = []
    for word in updated_words:
        if word in unique_words:
            index = unique_words.index(word)
            frequencies[index] += 1
        else:
            unique_words.append(word)
            frequencies.append(1)
    return unique_words, frequencies
    
# To display the results.
def print_frequencies(word, frequencies):
    print("\nWord Frequencies:")
for i in range(len(word)):
    print(word[i], ":", frequencies[i]) 

# Calls on functions to get a set sentence as input and calclate the frequency of each word in the sentence.
def main():
    user_sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)
