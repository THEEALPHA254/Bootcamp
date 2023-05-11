#outputs the letter with the most common frequency
import string

def most_common_letter(word):

    alphabet = string.ascii_lowercase
    dict = {}

    for letters in alphabet:
        dict[letters] = 0

    for letters in word:
        dict[letters] += 1

    dict = sorted(dict.items(), 
                        reverse=True, 
                        key=lambda x: x[1])

    for position in range(0, 26):
        print (dict[position])
        if position != len(dict) - 1:
            if dict[position + 1][1] < dict[position][1]:
                break

most_common_letter(input("Enter a word:"))
