#replace vowels with *
def replaceVowelsWithY(str, Y):
    vowels = 'AEIOUaeiou'
    for ele in vowels:
        str = str.replace(ele, Y)
 
    return str
input_str = "Theealpha"
 
Y = "*"
 
print("Given String:", input_str)
print("Specified character:", Y)
print("After replacing vowels with the specified character:",
      replaceVowelsWithY(input_str, Y))
