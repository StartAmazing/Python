def get_format_name(first, last, middle=''):
    '''Generate a neatly formatted full name'''
    if middle:
        return (first + " " + middle + " " + last).title()

    full_name = first + " " + last
    return full_name.title()
