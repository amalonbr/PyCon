class Dict:
    
    def __init__(self):
        self.n = 8
        self.karr = [[] for i in range(self.n)]
        self.varr = [[] for i in range(self.n)]
    
    def __setitem__(self, key, value):
        i = hash(key) % self.n
        self.karr[i].append(key)
        self.varr[i].append(value)
    
    def __getitem__(self, key):
        i = hash(key) % self.n
        try:
            j = self.karr[i].index(key)
        except ValueError:
            raise KeyError(key)
        return self.varr[i][j]

if __name__ == '__main__':
    
    d1 = Dict()
    d1['raymond'] = 'red'
    d1['rachel'] = 'blue'
    d1['mathew'] = 'yellow'
    print(d1['rachel'])
    
    d2 = Dict()
    d2['raymond'] = 'mac'
    d2['rachel'] = 'pc'
    d2['mathew'] = 'chromebook'
    print(d2['rachel'])
    
    d3 = Dict()
    d3['raymond'] = 'guitar'
    d3['rachel'] = 'flute'
    d3['mathew'] = 'piano'
    print(d3['rachel'])
    