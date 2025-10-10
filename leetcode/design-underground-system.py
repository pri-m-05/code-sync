class UndergroundSystem(object):

    def __init__(self):
        self.ppl = {}              
        self.stats = {}            

    def checkIn(self, id, stationName, t):
        self.ppl[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        startStation, t_in = self.ppl.pop(id)
        duration = t - t_in
        key = (startStation, stationName)
        if key not in self.stats:
            self.stats[key] = [0, 0]
        self.stats[key][0] += duration
        self.stats[key][1] += 1

    def getAverageTime(self, startStation, endStation):
        total, cnt = self.stats[(startStation, endStation)]
        return float(total) / cnt

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)