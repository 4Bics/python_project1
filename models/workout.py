#Creating a class for classes

class Workout:
  def __init__(self, name, type, duration, date, capacity, id=None):
    self.name = name
    self.type = type
    self.duration = duration
    self.date = date
    self.capacity = capacity
    self.id = id
    self.class_list = []
    self.instructors = []
  # def add_instructor(self, instructor):
  #   self.instructors.append(instructor.name)

  # def add_member_to_class(self, member):
  #   if len(self.class_list) < self.capacity:
  #     self.class_list.append(member.name)
  #   else:
  #     return "Class is fully booked!"