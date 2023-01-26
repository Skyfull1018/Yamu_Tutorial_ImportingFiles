
class TenmaCar:
    
    def __init__(self,speed):
       self.speed = speed
       self.brand = "Toyota"
       self.color = "Black"
            


    def CarRun(self):
        print(self.color, "色の",self.brand,"の車が",self.speed,"で走る")
    
    def CarStop(self):
        print(self.color, "色の車が止まる")






