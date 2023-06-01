class UndergroundSystem(object):

    def __init__(self):
        self.stationTime = {
            "ABC": {
                "DEF": []
            }}
        self.t = 0
        self.sys = {
            123: {
                "checkIn": (1, "Leyton"),
                "checkOut": (2, "Paradise")
            }
        }
        # self.stationTime["ABC"]["DEF"] = [0]

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if id not in self.sys.keys():
            self.sys[id] = {
                "checkIn": (t, stationName)
            }
        else:
            self.sys[id]["checkIn"] = (t, stationName)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.sys[id]["checkOut"] = (t, stationName)
        if self.sys[id]["checkIn"][1] not in self.stationTime.keys():
            self.stationTime[self.sys[id]["checkIn"][1]] = {
                self.sys[id]["checkOut"][1]: []
            }
        elif self.sys[id]["checkOut"][1] not in self.stationTime[self.sys[id]["checkIn"][1]].keys():
            self.stationTime[self.sys[id]["checkIn"][1]][self.sys[id]["checkOut"][1]] = []
        self.stationTime[self.sys[id]["checkIn"][1]][self.sys[id]["checkOut"][1]].append(
            self.sys[id]["checkOut"][0] - self.sys[id]["checkIn"][0])

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        # Type conversion to float is necessary
        avg = float(sum(self.stationTime[startStation][endStation])) / len(self.stationTime[startStation][endStation])
        # avg = sum(self.stationTime[startStation][endStation])/len(self.stationTime[startStation][endStation])
        # self.stationTime[startStation][endStation] = [avg]
        return avg


# Your UndergroundSystem object will be instantiated and called as such:
undergroundSystem = UndergroundSystem()
l1 = []
l1.append(undergroundSystem.checkIn(10, "Leyton", 3))
l1.append(undergroundSystem.checkOut(10, "Paradise", 8))  # Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
l1.append(undergroundSystem.getAverageTime("Leyton", "Paradise"))  # return 5.00000, (5)) / 1 = 5
l1.append(undergroundSystem.checkIn(5, "Leyton", 10))
l1.append(undergroundSystem.checkOut(5, "Paradise", 16))  # Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
l1.append(undergroundSystem.getAverageTime("Leyton", "Paradise"))  # return 5.50000, (5 + 6)) / 2 = 5.5
l1.append(undergroundSystem.checkIn(2, "Leyton", 21))
l1.append(undergroundSystem.checkOut(2, "Paradise", 30))  # Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
l1.append(undergroundSystem.getAverageTime("Leyton", "Paradise"))  # return 6.66667, (5 + 6 + 9) / 3 = 6.66667

print(l1)
