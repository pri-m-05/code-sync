class UndergroundSystem:

    def __init__(self):
        self.in_trip = {}
        self.stats = {}      

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_trip[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, time = self.in_trip.pop(id)
        key = (startStation, stationName)
        total, cnt = self.stats.get(key, (0, 0))
        total += (t - time)
        cnt += 1
        self.stats[key] = [total, cnt]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.stats[(startStation, endStation)]
        return total/count



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)