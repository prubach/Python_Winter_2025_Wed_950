my_file = 'data\\my_data.txt'

#with open(my_file, 'a') as f: # a - append at the end
with open(my_file, 'w') as f:  # w - overwrite
    f.write('hello world')
    f.write('\n')
    f.write('2nd line\n')
    f.write('3rd line\n')