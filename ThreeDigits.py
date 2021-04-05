import sys
from node_generation import action_space

#### Preprocessing Inputs

search_algo=sys.argv[1]
file_name=sys.argv[2]

text_file=open(str(file_name),"r")

input_parameters=[]
for x in text_file:
    input_parameters.append(x)

start=input_parameters[0].rstrip("\n")
goal=input_parameters[1].rstrip("\n")

forbidden_vals=[]
if len(input_parameters)==3:
    input_3=input_parameters[2].split(',')
    for i in input_3:
        forbidden_vals.append(str(i))

#### BEGIN PROCESSING NUMBERS

if search_algo=='B':
    if len(input_parameters)==3:
        action_space(start, goal, forbidden_vals).BFS()
    else:
        action_space(start, goal).BFS()
elif search_algo=='D':
    if len(input_parameters)==3:
        action_space(start, goal, forbidden_vals).DFS()
    else:
        action_space(start, goal).DFS()
elif search_algo=='I':
    if len(input_parameters)==3:
        action_space(start, goal, forbidden_vals).IDS()
    else:
        action_space(start, goal).IDS()
elif search_algo=='G':
    if len(input_parameters)==3:
        action_space(start, goal, forbidden_vals).Greedy()
    else:
        action_space(start, goal).Greedy()
elif search_algo=='A':
    if len(input_parameters)==3:
        action_space(start, goal, forbidden_vals).A_Star()
    else:
        action_space(start, goal).A_Star()
elif search_algo=='H':
    if len(input_parameters)==3:
        action_space(start, goal, forbidden_vals).HillClimb()
    else:
        action_space(start, goal).HillClimb()
else:
    print('Please specify one of the search methods: \'B\', \'D\', \'I\', \'G\', \'A\' or \'H\'.')
