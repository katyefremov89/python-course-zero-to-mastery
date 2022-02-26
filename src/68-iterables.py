# iterable - object or collection that can be iterated over (can be a dictionary, string , list , tuple, set, ect.)
# int cant be iterable, because it is not an object or collection of the items
# is dictionary is iterable?


# the output will be only the keys of the dictionary
users = {'name': 'Golem', 'age': 2000, 'can_swim': False}
for item in users:
    print(item)

# dictionaries have a built in function called items, to iterate through dictionary and get the pair of key and value:
# output is a tuples of keys and values
for item in users.items():
    print(item)

# another built in function is values
# output is the values of the dictionary
for item in users.values():
    print(item)

# another way to iterate is over keys
# output is a keys of the dictionary
for item in users.keys():
    print(item)

# if the output should be a key and a value (not a tuple) - possible to unpack tuples
for item in users.items():
    key, value = item
    print(key, value)

# possible to unpack tuples in the for loops
# short way to unpack tuples:
for key, value in users.items():
    print(key, value)