class Person(object):
    """ Parent class for doctors and patiets"""
    def __init__(self, first_name, last_name, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex