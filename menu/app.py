from .files.setup import setup
from . import debug


def elements_value_get(elem):
    p = [i[1] for i in elem]
    out = []
    for i in p:
        if i.startswith('link://'):
            p = ''.join(i.split('link://')[1:])
            if debug:
                print(p)
            p2 = p.split('.')[0]
            try:
                p = ''.join(p.split('.')[1:])
            except IndexError:
                try:
                    out.append(setup[p2])
                except KeyError:
                    out.append('Error')
            try:
                out.append(setup[p2][p])
            except KeyError:
                out.append('Error')
        else:
            out.append(i)
    return out


def elements_print(elem):
    list_ = elements_value_get(elem)
    out = [[i2[0], i] for i, i2 in zip(list_, elem)]
    return out


def element_get_value(elem):
    list_ = elements_value_get([elem])
    return list_[0]
