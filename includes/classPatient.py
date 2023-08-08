from classLocation import Location
from classTime import systemTime


class Patient(Location, systemTime):
    
    def __init__(self, id, priority, *args):
        super().__init__(*args)
        self.id = id
        self.priority = priority
    
    def getID(self):
        return self.id
    
    def getLocation(self):
        return Location.location
    
    def getPriority(self):
        return self.priority

    def SetPatientTime(self):
        return systemTime.getSystemTime