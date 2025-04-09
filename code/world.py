class Area:
    def __init__(self, name):
        self.name = name
        self.connecting_areas = []
        
class Zone:
    def __init__(self, name, area, travel_possible):
        self.name = name
        self.area = area
        self.travel_possible = travel_possible
        self.connecting_zones = []

class Location:
    def __init__(self):
        pass

    def __init__(self, area, zone):
        self.zone = zone
        self.area = area

    def move(self, zone):
        self.zone = zone

    def travel(self, area):
        self.area = area