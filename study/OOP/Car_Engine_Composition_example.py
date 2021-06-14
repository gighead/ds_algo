class Car:


    def __init__(self, model=None, color=None):
        self.model = model
        self.color = color

    def printDetails(self):
        print("Car Model:", self.model)
        print("Car Color:", self.color)

class SedanEngine:

    def start(self):
        print("Car has started")

    def stop(self):
        print("Car has stopped")


class Sedan(Car):

    def __init__(self, model, color):
        super().__init__(model, color)
        self.engine = SedanEngine()  #accessing other class objects in your class (owner class)

    def setStart(self):
        SedanEngine.start(self.engine)
        #self.engine.start() #both works

    def setStop(self):
        SedanEngine.stop(self.engine)
        #self.engine.stop()


