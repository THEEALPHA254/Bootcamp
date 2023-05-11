#Prints the longest common prefix in a string
string = ["green", "grey", "growing"]

def longestCommonPrefix(string):
    l = len(string[0])
    for i in range(1, len(string)):
        length = min(l, len(string[i]))
        while length > 0 and string[0][0:length] != string[i][0:length]:
            length = length - 1
            if length == 0:
                return 0
    return string[0][0:length]

print(longestCommonPrefix(string))