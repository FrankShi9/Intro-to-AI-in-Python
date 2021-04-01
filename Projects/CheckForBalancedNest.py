i = 0
input = '{[('
stack_0 = [ele for ele in input]

'''
def next():
    global stack, input, i
    if i< len(input):
        yield input[i]
    i+=1
'''

def checkBalance():

    global stack_0
    stack = []
    is_ba = True
    cnt = 0
    while ((is_ba and len(stack) != 0) or cnt == 0):
        try:
            ele = stack_0.pop(0)
            if (ord(ele) == ord('(')) or (ord(ele) == ord('{')) or (ord(ele) ==ord('[')):
                stack.append(ele)

            elif (ord(ele) == ord(')')) or (ord(ele) == ord('}')) or (ord(ele) == ord(']')):
                if len(stack)==0:
                    is_ba = False

                else:
                    buf = stack.pop()
                    test = buf+ele
                    if (test == '()') or (test =='{}') or (test =='[]'):
                        is_ba = True
                    else:
                        is_ba = False
        except IndexError:
            break
        cnt += 1

    if len(stack)!=0:
        is_ba = False

    return is_ba


if __name__ == '__main__':
    #(next().__next__())
    print(checkBalance())
    #print(stack_0)
    #print(ord('(') or ord('{') or ord('['))
    #print(ord(')'))
    #print('('+')')