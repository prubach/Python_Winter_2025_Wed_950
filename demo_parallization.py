from concurrent.futures.process import ProcessPoolExecutor
from functools import partial
from multiprocessing import Pool

from knotprot_download import *

def run_download_seq(my_dir):
    prot_list = get_proteins()
    i = 0
    for p in prot_list:
        download_link(my_dir, p)
        i += 1
    print(f'Done {i} downloads.')


def run_download_parall(my_dir):
    prot_list = get_proteins()
    download_func = partial(download_link, my_dir)
    #download_func(prot_list[0])
    with Pool(processes=4) as pool:
        pool.map(download_func, prot_list)

def run_thumbnails_seq(my_dir):
    file_list = Path(my_dir).iterdir()
    for f in file_list:
        create_thumbnail((256, 256), f)


def run_thumbnails_parall(my_dir):
    file_list = Path(my_dir).iterdir()
    create_thumbnail_func = partial(create_thumbnail, (256, 256))
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(create_thumbnail_func, file_list)


if __name__ == '__main__':
    my_dir = 'images'
    #setup_download_dir(my_dir)
    #time_it(run_download_seq, my_dir)
    #time_it(run_download_parall, my_dir)
    #time_it(run_thumbnails_seq, my_dir)
    time_it(run_thumbnails_parall, my_dir)