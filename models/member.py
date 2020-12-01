#Creating a class for member

class Member:
  def __init__(self, name, age, membership_type, enrolled_class, id=None):
    self.name = name
    self.age = age
    self.membership_type = membership_type
    self.enrolled_class = enrolled_class
    # self.class_credits = 0
    self.id = id