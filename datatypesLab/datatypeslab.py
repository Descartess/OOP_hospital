""" function to check the data type of supplied argument"""
def data_type(argument):
    """ function to check the data type of supplied argument"""
    if isinstance(argument, str):
        return len(argument)
    elif isinstance(argument, bool):
        return argument
    elif isinstance(argument, int):
        if argument == 100:
            return 'equal to 100'
        elif argument < 100:
            return 'less than 100'
        return 'more than 100'
    elif isinstance(argument, list):
        if len(argument) >= 3:
            return argument[2]
        return None
    elif callable(argument):
        argument(True)
        return True
    else:
        try:
            if argument is None:
                return 'no value'
        except NameError:
            return 'no value'
