""" Class to represent a car object """
class Car(object):
    """
    Class to represent a car object
    """

    def __init__(self, name="General", model="GM", car_type="saloon"):
        """
        initialises Car with default values for name, model and car type
        """
        self.car_type = car_type
        self.model = model
        self.name = name
        self.speed = 0

    @property
    def num_of_doors(self):
        """Return number of doors"""
        if self.name == "Porshe" or self.name == "Koenigsegg":
            return 2
        return 4

    @property
    def num_of_wheels(self):
        """Return number of wheels"""
        if self.car_type != "trailer":
            return 4
        return 8

    def is_saloon(self):
        """Return car type"""
        if self.car_type == "saloon":
            return True
        return False

    def drive(self, pedal_push):
        """ return object having speed"""
        if pedal_push == 3:
            self.speed = 1000
        elif pedal_push == 7:
            self.speed = 77
        return self
