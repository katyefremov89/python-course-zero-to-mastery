# def keyword defining a function
def say_hello():
    print('Hellllo')


say_hello()


# Functions that get parameters
def say_hello(name, emoji):
    print(f'{name} Hellllo {emoji}')


say_hello('Katy', ':/')

# The arguments are positional and position is matter - otherwise the output is not as expected


# Keyword arguments - arguments that created when the function is called
# Positional arguments - position is matter instead of keywords arguments


def say_hello(name, emoji):
    print(f'{name} Hellllo {emoji}')


say_hello(emoji=':/', name='Katy')  # output Katy Hellllo :/ even if not same position


# Default parameters are given when the function is defined,
# If the parameters are given when the function is called - function will use this parameters
# If not function will use default parameters that given when it was defined

def say_hello(name = 'Dart Vader', emoji = ':)'):
    print(f'{name} Hellllo {emoji}')


say_hello()  # output will be 'Dart Vader Hellllo :)'
say_hello('Bobo', ':>')  # output 'Bobo Hellllo :>'
say_hello('Kiki')  # output 'Kiki Hellllo :)'

# # # return # # #
# If there is no return statement - function will always return None
# Function either modifies the program or returns something


def sum_of_int(num1, num2):
    return num1 + num2


print(sum_of_int(1, 1))

# Function should do one thing really well or should return something

# Nested functions
