def setup(ns):
    ns['n'] = 8
    ns['karr'] = [[] for i in range(ns['n'])]
    ns['varr'] = [[] for i in range(ns['n'])]
    
def store(ns, key, value):
    i = hash(key) % ns['n']
    ns['karr'][i].append(key)
    ns['varr'][i].append(value)
    
def lookup(ns, key):
    i = hash(key) % ns['n']
    try:
        j = ns['karr'][i].index(key)
    except ValueError:
        raise KeyError(key)
    return ns['varr'][i][j]

if __name__ == '__main__':
    
    ns1 = {}
    setup(ns1)
    store(ns1, 'raymond', 'red')
    store(ns1, 'rachel', 'blue')
    store(ns1, 'mathew', 'yellow')
    print(lookup(ns1, 'rachel'))
    
    ns2 = {}
    setup(ns2)
    store(ns2,'raymond', 'mac')
    store(ns2, 'rachel', 'pc')
    store(ns2, 'mathew', 'chromebook')
    print(lookup(ns2, 'rachel'))
    
    ns3 = globals()
    setup(ns3)
    store(ns3,'raymond', 'guitar')
    store(ns3, 'rachel', 'flute')
    store(ns3, 'mathew', 'piano')
    print(lookup(ns3, 'rachel'))
    