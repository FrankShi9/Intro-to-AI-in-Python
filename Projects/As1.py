import csv
import numpy as np


csv_file_path = open('binary_data.csv') # set the file relative path
csv_reader = csv.reader(csv_file_path, delimiter=',') # instantiate a csv_reader

binary_data = np.zeros([100,6],dtype=int)  # the matrix used to store the binary data
N = 100  # This is the same N as specified in the task sheet


'''
loadFiletoMat() function loads the data from .csv file to the numpy matrix

para: input: matrix where the data will be stored
return void
'''


def load_file_mat(input):
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
            #print('loading stopped at row {}'.format(cnt - 1))
            break

        cnt += 1


'''
cnt_l() function counts the given l value: 0/1 within the binary data

para: l: value of l to be counted, input: matrix where the data will be read
return cnt_of_l: total count number of l with value l in the binary data
'''


def cnt_l(l: int, input):
    cnt_of_l = 0
    for index in range(0, 100):
        if input[index][5] == l:
            cnt_of_l += 1

    return cnt_of_l


'''
common_dis() function calculates the common distribution of l 
with value: 0/1 within the binary data

para: l: value of l to be calculated
return: common distribution of l = k
'''


def common_dis(l: int):
    if(l==1):
        return (l1 / N) # uses prestored count of l=1 to save time
    else:
        return (l0 / N) # uses prestored count of l=0 to save time


'''
cnt_a() function counts the occurrences of a(i)=a (i,a given as parameters) 
with l being value: l (l given as parameter) within the binary data

para: i: the subscript of a as the same in the task sheet 
      a: the value of a(i)
      l: value of l
      input: matrix where the data will be read
return: cnt_of_a: total count number of a(i) with value l=j in the binary data
'''


def cnt_a(i: int, a: int, l: int, input):
    cnt_of_a = 0
    for index in range(0, 100):
        if input[index][i] == a and input[index][5] == l:
            cnt_of_a += 1
    return cnt_of_a


'''
condi_dis() function calculates the conditional distribution 

para: i: the subscript of a as the same in the task sheet 
      a: the value of a(i)
      l: value of l
      input: matrix where the data will be read
return: conditional distribution 
'''


def condi_dis(i: int, a: int, l: int, input):
    if(l==0):
        return ((cnt_a(i, a, l, input) / l0))
    else:
        return ((cnt_a(i, a, l, input) / l1))


# main
if __name__ == '__main__':

    load_file_mat(binary_data)
    #print(bin)

    print('----------------------------------')  # separator

    # store the vars here to achieve dynamic programming
    l0 = cnt_l(0,binary_data)
    l1 = cnt_l(1,binary_data)

    # print the results of the two prior probabilities
    print('p(l={})={}'.format(0, common_dis(0)))  # output: 'p(l=0)=k' for instance

    print('p(l={})={}'.format(1, common_dis(1)))  # output: 'p(l=1)=k' for instance

    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=0|l=0)=k' for instance
        print('p(a{}={}|l={})={}'.format(i, 0, 0, condi_dis(i, 0, 0, binary_data)))

    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=1|l=0)=k' for instance
        print('p(a{}={}|l={})={}'.format(i, 1, 0, condi_dis(i, 1, 0, binary_data)))

    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=0|l=1)=k' for instance
        print('p(a{}={}|l={})={}'.format(i, 0, 1, condi_dis(i, 0, 1, binary_data)))

    print('----------------------------------')

    for i in range(0, 5):  # variable i the same as defined in worksheet
        # output: 'p(ai=1|l=1)=k' for instance
        print('p(a{}={}|l={})={}'.format(i, 1, 1, condi_dis(i, 1, 1, binary_data)))

    print('----------------------------------')


    #print(type(bin))

