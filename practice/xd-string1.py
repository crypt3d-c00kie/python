# Strings - Working with Textual Data

def main():
    message = "Method is just a function that belongs to an \"Object\""
    print(message[0:25:2]) # start:end:step
    
    # string_var.count() to count the number of occurences
    print(f"the letter {message[2]} is repeated {message.count(message[2])} time(s)")

    # string_var.find('input') to find the index of the first occurence
    print(f"the first occurence of \'function\' is at index {message.find('function')}")
    print(message[17:25])

    # string_var.replace('find', 'replace') to find the word and replace
    print(f"Find '\Method'\ and Replace it with \'Potato\'")
    print(f"Before :: {message}")
    print(f"Function Call :: {message.replace('Method', 'Potato')}")
    print(f"After :: {message}")

    # concatenation and placeholders
    word1 = "After"
    word2 = "Effects"
    print(word1 + ', ' + word2)
    # string_var.format(replacePlaceHolder1, replacePlaceHolderN)
    sentence = "{} {} is really amazing!".format(word1,word2)
    # alternatively f strings can be used
    print(sentence)

    # string_var.upper() and string_var.lower()
    sentence = f"{word1.upper()} {word2.lower()} is really amazing!"
    print(sentence)
    
    # dir(var) to access the list of usable methods
    # print(dir(word2))
    # its following output
    '''
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
        '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
        '__getitem__', '__getnewargs__', '__gt__', '__hash__',
        '__init__', '__init_subclass__', '__iter__', '__le__',
        '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
        '__new__', '__reduce__', '__reduce_ex__', '__repr__',
        '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
        '__str__', '__subclasshook__', 'capitalize', 'casefold',
        'center', 'count', 'encode', 'endswith', 'expandtabs',
        'find', 'format', 'format_map', 'index', 'isalnum',
        'isalpha', 'isdecimal', 'isdigit', 'isidentifier',
        'islower', 'isnumeric', 'isprintable', 'isspace',
        'istitle', 'isupper', 'join', 'ljust', 'lower',
        'lstrip', 'maketrans', 'partition', 'replace',
        'rfind', 'rindex', 'rjust', 'rpartition',
        'rsplit', 'rstrip', 'split', 'splitlines',
        'startswith', 'strip', 'swapcase', 'title',
        'translate', 'upper', 'zfill']
    '''

    # alternatively help(var_type) can be used to view much more descriptive version
    # print(help(type(word1)))
    # help(var_type.lower()) to view a brief description of certain method
    print(help(type(word1).upper))


if __name__ == '__main__':
    main()