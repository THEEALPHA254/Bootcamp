#sorting the list of dictionaries by key='name'
from operator import itemgetter
dict_to_be_sorted=[{'name': 'Zozo', 'age': '20'}, {'name': 'Grace', 'age': 19}, {'name': 'Sam', 'age': 35}]
newdict = sorted(dict_to_be_sorted, key=itemgetter('name'))
print(newdict)