#Creating a class for instructor

class Instructor:
  def __init__(self, name, age, id=None):
    self.name = name
    self.age = age
    self.classes = []
    self.id = id