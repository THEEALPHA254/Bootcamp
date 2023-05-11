#Outputs th esecond largest integer in a list
def second_largest(list):
    list.sort()
    return list[-2]

li=[]
n=int(input("Num of items:"))
for i in range(0,n):
    a=int(input("Enter a number:"))
    li.append(a)

li.sort(reverse=True)
print("sorted list in descending order:", li) 
print("second largest in ",li,"is")
print(second_largest(li))     
     