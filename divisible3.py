#SUm of numbers divisible by 3
sum = 0
for i in range(10):
    if i % 3 == 0:
        sum = sum + i
print("sum=", sum)