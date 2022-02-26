# python can convert values to be truthy or falsey
# example
# interpreter converts the type (int or string) to boolean -> bool(5)
is_old = 5
is_licenced = 'Yes'

# the if statement will return true
if is_old and is_licenced:
    print('u r old enough to drive and u have a licence!')
else:
    print('u r not of age!')

# the output will be true - Truthy value
print(bool(5))

# the output will be false - Falsey value 
print(bool(0))
print(bool(''))
