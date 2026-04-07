class Robot:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.p = 2 * (width + height) - 4
        self.path = []

        for x in range(width):
            self.path.append((x, 0))
        for y in range(1, height):
            self.path.append((width - 1, y))
        for x in range(width - 2, -1, -1):
            self.path.append((x, height - 1))
        for y in range(height - 2, 0, -1):
            self.path.append((0, y))

        self.i = 0
        self.moved = False

    def step(self, num):
        self.i = (self.i + num % self.p) % self.p
        self.moved = True

    def getPos(self):
        x, y = self.path[self.i]
        return [x, y]

    def getDir(self):
        x, y = self.path[self.i]

        if x == 0 and y == 0:
            return "South" if self.moved else "East"
        if y == 0:
            return "East"
        if x == self.w - 1:
            return "North"
        if y == self.h - 1:
            return "West"
        return "South"