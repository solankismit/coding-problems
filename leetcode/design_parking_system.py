# Design Parking System
class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        # First ATTEMPT
        # self.parkingarea={'big':big,'medium':medium,'small':small}

        # Second ATTEMPT
        # self.big=big
        # self.medium=medium
        # self.small=small

        # Third ATTEMPT
        self.carType = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        # First ATTEMPT
        # cartype= {1:'big',2:'medium',3:'small'}
        # if self.parkingarea[cartype[carType]]>0:
        #     self.parkingarea[cartype[carType]]-=1
        #     return True
        # return False

        # Second ATTEMPT
        # if (carType == 1 and self.big == 0) or (carType == 2 and self.medium == 0) or (carType == 3 and self.small == 0):
        #     return False
        # elif carType==1:
        #     if self.big>0:
        #         self.big-=1
        #         return True
        #     return False
        # elif carType==2:
        #     if self.medium>0:
        #         self.medium-=1
        #         return True
        #     return False
        # elif carType==3:
        #     if self.small>0:
        #         self.small-=1
        #         return True
        #     return False
        # else:
        #     return False

        # Third ATTEMPT
        if self.carType[carType - 1] > 0:
            self.carType[carType - 1] -= 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)