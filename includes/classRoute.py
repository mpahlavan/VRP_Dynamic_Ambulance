from classLocation import Location

class Route(Location):
    
    def __init__(self, id_vehicle, Location, Patient_num):
        self.id_vehicle = id_vehicle
        self.Location = Location
        self.patient_num = Patient_num

    def getVehicle(self):
        return self.id_vehicle
    
    def getPatient(self):
        return self.patient_num
    
    def getDistance(self, ):
        return self.longtitude, self.latitude