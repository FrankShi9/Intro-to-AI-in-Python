
#strings in python are immutable!!

#list

a = ['a','b','c']
a += ['d']
#print(a)
#print('d' in a)
#print(a.sort())

def returnList(input):
    buf = list(input)
    return buf.pop(0)



#dict: using strings as index instead of ints
#basic data structure: Hash table
def dictOps():
    alphabet = {"a":"alpha", "b":"beta"}
    print(alphabet["a"])
    print(alphabet.keys())
    print(alphabet.values())
    for value in alphabet.values():
        print(value)

if __name__ == '__main__':
    #dictOps()
    print(returnList(a))