input = 'geeksforgeeks'
output = set()
for char in input:
    output.add(char)
print(output)

result_list = []
unique_set = set(input)
for ele in input:
    if ele in unique_set:
        result_list.append(ele)
        unique_set.remove(ele)
print(result_list)