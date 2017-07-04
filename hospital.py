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

class Hospital(object):
    def __init__(self, name):
        self.name = name
        self.num_of_docs = 0
        self.num_of_patients = 0
        self.doctors = {}
        self.patients = {}

    def add_doctor(self,first_name, last_name, sex):
        """ hire doctors """
        doc = Doctor(first_name, last_name, sex)
        self.doctors[self.num_of_docs] = doc
        self.num_of_docs +=1

    def add_patient(self,first_name, last_name, sex):
        """ check in patients """
        pat = Patient(first_name, last_name, sex)
        self.doctors[self.num_of_patients] = pat
        self.num_of_patients +=1



    