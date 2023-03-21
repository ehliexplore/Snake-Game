def record(file, points):
    a = open(file, 'at')
    if points > p:
        a.write(f'{points}')
        print(points)
    a.close()


def read(file):
    global p
    a = open(file, 'rt')
    p = int(a.read())
    return p




