# range function is very useful in for loops
# besides lists, dictionaries, etc. it is possible to iterate also over a range
# Example:
for item in range(100):
    print(item)
# it is possible not to use iterable variable (item)
# Example:

for _ in range(100):
    print(_)

# range functions comes with 3rd parameter - step over (step over iterated numbers)
# Example:
for item in range(0, 10, 2):
    print(item)

# iterating in reverse
for item in range(10, 0, -1):
    print(item)


# enumerate - useful if we need the index counter of the item we are looping through
for i, char in enumerate((1, 2, 3, 4, 5)):
    print(i, char)

# Exercise - enumerate a list with range 100 and print the index of 50
for i, number in enumerate(list(range(100))):
    if number == 50:
        print(f'index of 50 is: {i}')
