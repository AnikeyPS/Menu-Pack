from .files.setup import setup


def elements_value_get(elem):
    p = [i[1] for i in elem]
    out = []
    for i in p:
        if 'link://' in i:
            p = i.split('link://')[1]
            p2 = p.split('.')[0]
            try:
                p = p.split('.')[1]
            except IndexError:
                try:
                    out.append(setup[p2])
                except KeyError:
                    out.append('Error')
            try:
                out_ = setup[p2][p]
                out_ = 'pycommand: ' + out_.split('command://')[1]
                out.append(out_)
            except KeyError:
                out.append('Error')
        else:
            if 'command://' in i:
                out_ = i
                out_ = 'pycommand: ' + out_.split('command://')[1]
                out.append(out_)
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
