# Short circuiting - happens when the interpreter is smart enough,
# when the first statement is Truthy the interpreter know to skip the second statement
# Example:

is_human = True
is_friend = True

# the compiler will check the first statement of the if and right after will print
if is_human or is_friend:
    print('can be friend')  # will be printed

# same behaviour as before
is_human = False
if is_human and is_friend:
    print('can be friend')  # wont be printed
