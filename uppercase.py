#change the cases to uppercase
def uppercase(my_list):
    return [x.upper() for x in my_list]
a =(input("Enter strings:"))
b =(input("Enter strings:"))
c =(input("Enter strings:"))
print(uppercase([a,b,c]))