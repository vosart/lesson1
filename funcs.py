def get_summ(one, two, delimeter='&'):
    one = str(one)
    two = str(two)
    return f'{one}{delimeter}{two}' 
    # либо в одну строку
    # return '{0}{1}{2}'.format(str(one), delimeter, str(two))

result = get_summ('Learn', 'python')
print(result)
print(result.upper())
