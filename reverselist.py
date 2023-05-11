#reverse a a list of strings
def reverse(list):
    return [x [::-1] for x in list]
a =(input("Enter string:"))
b =(input("Enter string:"))
c =(input("Enter string:"))
print(reverse([a, b, c]))