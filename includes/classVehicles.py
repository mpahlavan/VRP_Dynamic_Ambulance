from classLocation import Location
from classTime import systemTime
from classPatient import Patient


class Vehicle(Location, systemTime):
    def __init__(self, id, type, speed,  fuel, availability, capacity, *args):
        super().__init__(*args)

        self.id = id
        self.type = type
        self.speed = speed
        self.availablity = availability
        self.capacity = capacity

    def getID(self):
        return self.id

    def getAvailability(self):
        return self.availablity
    
    def setAvailability(self):
        if self.availablity:
            self.availablity = 0
        else:
            self.availablity = 1

    def getFuel(self):
        return self.fuel

    def getCapacity(self):
        return self.capacity

    def setCapacity(self):
        #TODO: check in the patientList to set capacity
        self.capacity -= 1