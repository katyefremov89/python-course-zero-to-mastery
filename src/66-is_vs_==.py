# == - checks for equality (or equality of value)
# is - 'True is 1' - will check the location in memory this value is stored is the same

print(True == 1)  # output True
print('' == 1)  # output False

print(True is 1)  # output False
print(True is True)  # output True


# works different with lists, datasets or objects - every time list is created - new location in memory is allocated
print([] is [])  # output will be False
print([] == [])  # output will be True

