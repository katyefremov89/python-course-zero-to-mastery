# Find duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
duplicates = []

while len(some_list) >= 1:
    var = some_list.pop()
    for item in some_list:
        if item == var and item not in duplicates:
            duplicates.append(item)

print(duplicates)


# Another solution
for item in some_list:
    if some_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print(duplicates)