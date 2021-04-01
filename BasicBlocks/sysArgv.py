import sys
'''
item compute 1/(i!)
para: integer i
return 1/(i!)
'''
def item(i):
    #calculate i/(0!)
    if i == 0 or i == 1:
        return 1

    #compute 1/(i!)
    fact = 1.0
    for i in range(2, ++i):
        fact *= i

    return 1.0/fact

if __name__ == '__main__':
    print(sys.argv)

    # 1 + 1 + 1/2! + \cdots + 1/n!
    if len(sys.argv) < 2:
        exit(0)

    # sys.argv[0] is the name of script.
    n = int(sys.argv[1])

    s = 1
    item = 1

    for i in range(1,n+1):
        item *= 1.0/i
        s+=item

    print('e is %.10f'%s)