#Creating a class for member

class Member:
  def __init__(self, name, age, membership_type):
    self.name = name
    self.age = age
    self.membership_type = membership_type
    self.enrolled_classes = []
    self.class_credits = 0