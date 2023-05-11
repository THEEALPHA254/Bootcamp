#OUtputs sum of first elements in a tuple where the second element is even
def sum_first_even_tuples(tuple):
    sum = 0
    for tup in tuple:
        if tup[1] % 2 == 0:
            sum += tup[0]
    return sum


tuple = [(3, 8), (5, 1), (6, 2), (7, 9)]
result = sum_first_even_tuples(tuple)
print("Sum of first elements where second element is even is:", result)
