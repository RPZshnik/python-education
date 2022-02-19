import re

find_members = []

for function in dir(re):
    if "find" in function:
        find_members.append(function)

find_members.sort()
print(find_members)
