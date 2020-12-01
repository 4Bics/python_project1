#Creating a class for instructor

class Instructor:
  def __init__(self, name, age, workout, id=None):
    self.name = name
    self.age = age
    self.workout = workout
    self.id = id