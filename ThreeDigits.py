import sys

search_algo=sys.argv[1]
file_name=sys.argv[2]

text_file=open(str(file_name),"r")

start=text_file.readline()
goal=text_file.readline()

# BEGIN PROCESSING NUMBERS

print('Start', start)
print('Goal', goal)