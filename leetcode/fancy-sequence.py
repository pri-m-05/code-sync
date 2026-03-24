class Fancy(object):
    def __init__(self):
        self.mod = 10**9 + 7
        self.vals = []
        self.mul = 1
        self.add = 0

    def append(self, val):
        inv = pow(self.mul, self.mod - 2, self.mod)
        x = (val - self.add) % self.mod
        x = (x * inv) % self.mod
        self.vals.append(x)

    def addAll(self, inc):
        self.add = (self.add + inc) % self.mod

    def multAll(self, m):
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx):
        if idx >= len(self.vals):
            return -1
        return (self.vals[idx] * self.mul + self.add) % self.mod