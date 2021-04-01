age = 21.141592657

if __name__ == '__main__':
    print('my age is ' + f'{age}')
    print('my age is {1} {0} {1} {tom}'.format(age, 22.1, tom='cat'))
    print('my age in dec is %d' %int(age))
    print('my age in oct is %o' %int(age))
    print('my age in hex is %x' %int(age))
    print('my age in float is %.7g' %age)