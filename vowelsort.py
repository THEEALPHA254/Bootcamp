#sorts the strings depending on the number of vowels they contain
list = ['banana', 'apple', 'pineapple']
print (sorted(list,key=lambda word: sum(x in 'aeiou' for x in word),
        reverse=True))