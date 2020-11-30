import unittest
from models.instructor import Instructor

class TestInstructor(unittest.TestCase):
  def setUp(self):
    self.instructor = Instructor("Emily", 21)

#Test instructor has name
  def test_instructor_has_name(self):
    self.assertEqual("Emily", self.instructor.name)

#Test instructor has age
  def test_instructor_has_age(self):
    self.assertEqual(21, self.instructor.age)