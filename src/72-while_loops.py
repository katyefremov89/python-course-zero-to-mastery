# possible to create an endless loops with while loop if there is no break or variable increment
# possible to add else condition for the while loop
# using for and while loops:
# for loops are better for iterated objects
# while loops are better to use when we dont know how much we will be iterating over
i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('Done')


# possible to loop with while True and break the loop at the condition
# Example:
while True:
    response = input('say HI! ')
    if response == 'bye':
     break