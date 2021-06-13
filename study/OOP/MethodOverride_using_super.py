class Shape:

    def __init__(self, name):
        self.sname = name

    def getName(self):
        return self.sname

class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return (super().getName() + "," + " " +self.xsname)