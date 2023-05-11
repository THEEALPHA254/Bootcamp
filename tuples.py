# Sort the list of tuples by second element
tuples = [(2020, 'Thee'), (1996, 'Alpha'), (2030, 'Kenya')]
sorted_list = sorted(tuples, key=lambda x: x[1])
print(sorted_list)

