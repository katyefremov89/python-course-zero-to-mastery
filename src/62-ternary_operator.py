# Ternary operator - shortcuts that helps to make a code cleaner (also called conditional expressions)
# Expression - something that evaluates to a value
# condition_is_true if condition else condition_if_else
# First the interpreter will check if condition - > if true do condition_is_true else do condition_if_else
# Example:

is_friend = True

# depends on if is_friend 
can_message = 'message allowed' if is_friend else 'not allowed to message'
print(can_message)