modules_dict = {}
__ver__ = '0.1'

def add_module (name, ver):
    print (f': {name}.py \n:: {ver}')

    modules_dict [name] = ver

add_module (__name__, __ver__)
