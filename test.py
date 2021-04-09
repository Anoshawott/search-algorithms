# thing=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

# if [5,6] in thing:
#     print('working')


# print(thing)

# value='123'

# print([int(char) for char in value])

from collections import defaultdict

data_dict = defaultdict(list)

data_dict['test'].append('values and attributes')
data_dict['test'].append('more stuff')


print(data_dict)
