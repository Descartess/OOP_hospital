""" Tests for hospital oop design """
import unittest
from hospital import Person, Patient, Doctor

class TestPerson(unittest.TestCase):
    """ tests for the Person class """
    def setUp(self):
        self.person = Person('Paul', 'Nyondo', 'M')

    def testperson(self):
        """ test the __init__ method """
        self.assertEqual([self.person.first_name, self.person.last_name,
        self.person.sex],['Paul','Nyondo','M'])

class TestDoctor(unittest.TestCase):
    """ tests for the Doctor class """
    def setUp(self):
        self.doc = Doctor('Morgan', 'Freeman', 'M')
    def testdoc(self):
        """ tests for the __init__ method """
        self.assertEqual([self.doc.first_name, self.doc.last_name,
        self.doc.sex],['Morgan','Freeman','M'])

class TestPatient(unittest.TestCase):
    """ tests for the Patient class """
    def setUp(self):
        self.patient = Patient('Jon', 'Snow', 'M')
    def testpatient(self):
        """ tests for the __init__ method """
        self.assertEqual([self.patient.first_name, self.patient.last_name,
        self.patient.sex],['Jon','Snow','M'])
    def testssickeness(self):
        """ checks if admitted patient is sick"""
        self.assertTrue(self.patient.sick)

unittest.main()
