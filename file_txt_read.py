my_file = 'data/my_data.txt'

f = open(my_file, 'r')
i = 0
for line in f:
    i = i + 1
    print(f'{i}: {line}', end='')
f.close()


# with open(my_file, 'r') as f:
#     i = 0
#     for line in f:
#         i = i + 1
#         print(f'{i}: {line}', end='')
