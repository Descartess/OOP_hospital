class Person(object):
    """ Parent class for doctors and patients"""
    def __init__(self, first_name, last_name, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

class Patient(Person):
    """ class to handle all patient methods """
    def __init__(self, first_name, last_name, sex):
        """initialise the doctor class """
        super(Patient, self).__init__(first_name, last_name, sex)
        self.sick = True

class Doctor(Person):
    """ class to handle all patient methods """
    def __init__(self, first_name, last_name, sex):
        """initialise the doctor class """
        super(Doctor, self).__init__(first_name, last_name, sex)
    