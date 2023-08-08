import os
from datetime import datetime

class systemTime:

    def __init__(self):
        now = datetime.now()
        self.systemTime = now.strftime("%H:%M:%S")


    def getSystemTime(self):
        return self.systemTime
    