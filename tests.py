""" Tests for hospital oop design """
import unittest
from hospital import Person, Patient , Doctor 

class TestPerson(unittest.TestCase):
    """ tests for the Person class """
    def setUp(self):
        self.person = Person('Paul', 'Nyondo', 'M')

    def testperson(self):
        """ test the __init__ method """
        self.assertEqual([self.person.first_name, self.person.last_name,
        self.person.sex],['Paul','Nyondo','M'])

class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.doc = Doctor('Morgan', 'Freeman', 'M')
    def testdoc(self):
        self.assertEqual(self.doc.first_name, self.doc.last_name,
        self.doc.sex,['Morgan','Freeman','M'])

unittest.main()
