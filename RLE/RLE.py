

def encode(mess):
    if not mess : return ''

    old = mess[0]
    i = 1
    res = []

    for c in mess[1:]:
        if c != old:
            res.append(f'{i}{old}')
            i = 1
            old = c
        else:
            i += 1
    res.append(f'{i}{old}')

    return ''.join(res)
