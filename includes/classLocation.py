class Location:
    def __init__(self, longtitude, latitude):
        self.longtitude = longtitude
        self.latitude = latitude
    
    def getLocation(self):
        return (self.longtitude, self.latitude)