# input = 'geeksforgeeks'
# output = set()
# for char in input:
#     output.add(char)
# print(output)
#
# result_list = []
# unique_set = set(input)
# for ele in input:
#     if ele in unique_set:
#         result_list.append(ele)
#         unique_set.remove(ele)
# print(result_list)
# import numpy as np
#
# mat = np.zeros((2726,2097352), int)
#
# r, c = np.shape(mat)
#
# print(r,c)
#
# mat [0] [0] = 1
#
# print(mat)
# print('h\n')
# print('\n')
# print('f\n')

# text = ['h\n','\n','f\n']
#
# filename = 'test.txt'
# with open(filename, 'w') as file_object:
#     for ele in text:
#         file_object.write(ele)
# print([[1] for i in range (0,2)])
a = [1,2,2,3,3]
b = list(set(a))
print(b)
b = []
for ele in a:
    if ele not in b:
        b.append(ele)
print(b)
