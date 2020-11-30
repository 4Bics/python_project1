#Creating a class for classes

class Workout:
  def __init__(self, name, type, duration, date, capacity):
    self.name = name
    self.type = type
    self.duration = duration
    self.date = date
    self.instructors = []
    self.capacity = capacity
    self.class_list = []

  def add_instructor(self, instructor):
    self.instructors.append(instructor.name)

  def add_member(self, member):
    self.class_list.append(member.name)