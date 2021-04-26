class exercises:
    def __init__(self, name, cal, time):
        self.name = name
        self.cal = cal
        self.time = int(time)

    def getcal(self):
        return self.cal

    def gettime(self):
        return self.time

    def getname(self):
        return self.name