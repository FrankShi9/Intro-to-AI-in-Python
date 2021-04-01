import csv
import copy
import numpy as np

csv_file_path = open('binary_data.csv')

csv_reader = csv.reader(csv_file_path, delimiter=',') #

#binary_data = []
#binary_data_1 = []
bin = np.zeros([100,6],dtype=int) # the matrix used to store the binary data

N = 100

'''
def printList(input):
    cnt = 0
    print('[')

    for row in range(0,100):
        if cnt % 6 ==0:
            print(input[row])
            #print('\n')
        else:
            print(input[row])
        cnt+=1

    print(']')
'''
'''
def printFile():
    cnt = 1
    while (True):
        try:
            print(cnt, csv_reader.__next__())

        except StopIteration:
            print('printing stopped at row {}'.format(cnt - 1))
            break

        cnt += 1
'''
'''
def loadFiletoList(): #add a input para here
    cnt = 1
    while (True):
        try:
            binary_data.append(csv_reader.__next__())

        except StopIteration:
            print('loading stopped at row {}'.format(cnt - 1))
            break

        cnt += 1
'''


'''
loadFiletoMat function loads the data from .csv file to the numpy matrix
para: input matrix where the data will be stored
return void
'''
def loadFiletoMat(input): #
    cnt = 1
    col,row = 0,0
    while (True):
        tmp = []
        try:
            tmp.append(csv_reader.__next__())
            for ele in tmp[0]:
                input[row][col] = int(ele)
                col+=1

            row += 1
            col = 0
        except StopIteration:
            print('loading stopped at row {}'.format(cnt - 1))
            break

        cnt += 1

'''
def convert(): #add a input para here
    global binary_data_1
    binary_data_1 = copy.deepcopy(binary_data)
    for i in range(0, 100):
        for ele in range(0, 6):
            if binary_data_1[i][ele] == str(1):
                binary_data_1[i][ele] = 1
            else:
                binary_data_1[i][ele] = 0
'''

'''
def verify(input1, input2): #add a input para here
    #global binary_data, binary_data_1
    for i in range(0, 100):
        for ele in range(0, 6):
            if input1[i][ele] != input2[i][ele]:
                return False

    return True
'''

def cnt_l(i: int, input):
    cnt_of_i = 0
    for index in range(0, 100):
        if input[index][5] == i:
            cnt_of_i += 1

    return cnt_of_i



def commonDis(i: int):
    if(i==1):
        return (l1 / N)
    else:
        return (l0 / N)


def cnt_a(i: int, a: int, l: int, input):
    cnt_of_a = 0
    for index in range(0, 100):
        if input[index][i] == a and input[index][5] == l:
            cnt_of_a += 1
    return cnt_of_a


def condi_dis(i: int, a: int, l: int, input):
    if(l==0):
        return ((cnt_a(i, a, l, input) / l0))
    else:
        return ((cnt_a(i, a, l, input) / l1))


# main
if __name__ == '__main__':

    #printFile()
    #loadFiletoList()  # load the file content into list: binary_data
    #convert()  # convert the file from 2D list consisting of strings to !!!
    #print(binary_data)
    #print(binary_data_1)
    #printList(binary_data_1)
    #print('Are the converted data authentic? ', verify())


    loadFiletoMat(bin)
    #print(bin)

    print('----------------------------------')  # separator

    # store the vars here to achieve dynamic programming
    l0 = cnt_l(0,bin)
    l1 = cnt_l(1,bin)

    # print the results of the two prior probabilities
    print('p(l={})={}'.format(0, commonDis(0)))  # p(l=0)=k for instance

    print('p(l={})={}'.format(1, commonDis(1)))  # p(l=1)=k for instance

    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet

        print('p(a{}={}|l={})={}'.format(i, 0, 0, condi_dis(i, 0, 0, bin)))  # p(ai=0|l=0)=k for instance

    print('----------------------------------')

    for i in range(0, 5):
        print('p(a{}={}|l={})={}'.format(i, 1, 0, condi_dis(i, 1, 0, bin)))  # p(ai=1|l=0)=k for instance

    print('----------------------------------')

    for i in range(0, 5):
        print('p(a{}={}|l={})={}'.format(i, 0, 1, condi_dis(i, 0, 1, bin)))  # p(ai=0|l=1)=k for instance

    print('----------------------------------')

    for i in range(0, 5):
        print('p(a{}={}|l={})={}'.format(i, 1, 1, condi_dis(i, 1, 1, bin)))  # p(ai=1|l=1)=k for instance

    print('----------------------------------')

    #print(type(bin))

