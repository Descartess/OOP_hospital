""" returns fizzBuzz if divisible by 3 and 5
    returns fizz if divisible by 3
    returns Buzz if divisible by 5
"""
def fizz_buzz(arg):
    """ returns fizzBuzz if divisible by 3 and 5
        returns fizz if divisible by 3
        returns Buzz if divisible by 5
    """
    if isinstance(arg, int) and arg > 0:
        if arg % 3 == 0 and arg % 5 == 0:
            return 'fizzBuzz'
        elif arg % 3 == 0:
            return 'fizz'
        elif arg % 5 == 0:
            return 'buzz'
        else:
            return arg
    else:
        return 'Invalid Argument'
