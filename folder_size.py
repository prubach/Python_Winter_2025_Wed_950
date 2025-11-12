#my_folder = '.venv'
import os.path

my_folder = 'data'

def compute_folder_size(my_folder):
    # with the content
    os.path.isdir(my_folder) # if it is a directory
    os.path.isfile(my_folder) # if it is a regular file
    os.path.getsize(my_folder) # get the size of a file
    return


print(f'size of folder "{my_folder}": {compute_folder_size(my_folder)}')