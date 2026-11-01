class UndergroundSystem:

    def __init__(self):
        self.hm1 = {}
        self.hm2 = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.hm1[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        entry_station, entry_time = self.hm1[id]

        travel_time = t - entry_time

        key = (entry_station, stationName)

        if key not in self.hm2:
            self.hm2[key] = [0,0]

        self.hm2[key][0]+=travel_time
        self.hm2[key][1]+=1

        del self.hm1[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)

        totalTime, count = self.hm2[key]

        return totalTime/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)