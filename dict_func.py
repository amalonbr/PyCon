def setup():
    global n, karr, varr
    n = 8
    karr = [[] for i in range(n)]
    varr = [[] for i in range(n)]
    
def store(key, value):
    i = hash(key) % n
    karr[i].append(key)
    varr[i].append(value)
    
def lookup(key):
    i = hash(key) % n
    try:
        j = karr[i].index(key)
    except ValueError:
        raise KeyError(key)
    return varr[i][j]

if __name__ == '__main__':
    setup()
    store('raymond', 'red')
    store('rachel', 'blue')
    store('mathew', 'yellow')
    print(lookup('rachel'))
    