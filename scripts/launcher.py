import os

from os.path import expanduser

path = expanduser("~") + '/.config/conky/'
for i in filter(
        lambda x: len(x.split('.')) > 1 and x.split('.')[1] == 'conf',
        os.listdir(path)
):
    os.system(f'conky -c {path}/{i}')
