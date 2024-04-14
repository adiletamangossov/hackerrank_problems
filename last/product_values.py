import numpy as np


def product_dict_values(my_dict):
    return np.prod(list(my_dict.values()))


if __name__ == '__main__':
    dictionary = {'x': 30, 'y': 45, 'z': 13}
    print(product_dict_values(dictionary))
