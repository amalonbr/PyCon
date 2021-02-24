class Dict:
    
    def setup(self):
        self.n = 8
        self.karr = [[] for i in range(self.n)]
        self.varr = [[] for i in range(self.n)]
    
    def store(self, key, value):
        i = hash(key) % self.n
        self.karr[i].append(key)
        self.varr[i].append(value)
    
    def lookup(self, key):
        i = hash(key) % self.n
        try:
            j = self.karr[i].index(key)
        except ValueError:
            raise KeyError(key)
        return self.varr[i][j]

if __name__ == '__main__':
    
    d1 = Dict()
    d1.setup()
    d1.store('raymond', 'red')
    d1.store('rachel', 'blue')
    d1.store('mathew', 'yellow')
    print(d1.lookup('rachel'))
    
    d2 = Dict()
    d2.setup()
    d2.store('raymond', 'mac')
    d2.store('rachel', 'pc')
    d2.store('mathew', 'chromebook')
    print(d2.lookup('rachel'))
    
    d3 = Dict()
    d3.setup()
    d3.store('raymond', 'guitar')
    d3.store('rachel', 'flute')
    d3.store('mathew', 'piano')
    print(d3.lookup('rachel'))
    