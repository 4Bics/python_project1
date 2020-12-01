import unittest

from models.workout import Workout
from models.member import Member
from models.instructor import Instructor

class TestWorkout(unittest.TestCase):
  def setUp(self):
    self.workout = Workout("Fuego", "HIIT", "45 minutes", "5th December 2020", 3)
    self.instructor = Instructor("Emily", 21)
    self.member = Member("Cameron", 25, "Gold")
  
#Test workout has name
  def test_workout_has_name(self):
    self.assertEqual("Fuego", self.workout.name)

#Test workout has type
  def test_workout_has_type(self):
    self.assertEqual("HIIT", self.workout.type)

#Test workout has duration 
  def test_workout_has_duration(self):
    self.assertEqual("45 minutes", self.workout.duration)

#Test workout has date 
  def test_workout_has_date(self):
    self.assertEqual("5th December 2020", self.workout.date)

#Test workout has capacity 
  def test_workout_has_capacity(self):
    self.assertEqual(3, self.workout.capacity)

#Test unsaved has none id
  def test_workout_has_none_id(self):
    self.assertEqual(None, self.workout.id)

# #Test add instructor to workout 
#   def test_add_instructor(self):
#     self.workout.add_instructor(self.instructor)
#     self.assertEqual(1, len(self.workout.instructors))

# #Test add member to workout 
#   def test_add_member(self):
#     self.workout.add_member_to_class(self.member)
#     self.assertEqual(1, len(self.workout.class_list))

# #Test add member to workout - class is full
#   def test_add_member_class_full(self):
#     self.workout.add_member_to_class(self.member)
#     self.workout.add_member_to_class(self.member)
#     self.workout.add_member_to_class(self.member)
#     self.assertEqual("Class is fully booked!", self.workout.add_member_to_class(self.member))
#     self.assertEqual(3, len(self.workout.class_list))
