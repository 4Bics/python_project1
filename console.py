import pdb

from models.instructor import Instructor
from models.member import Member
from models.workout import Workout

import repositories.workout_repository as workout_repository

workout_repository.delete_all()
# instructor_repository.delete_all()
# member_repository.delete_all()

# instructor_1 = Instructor("Emily", 21)
# instructor_repository.save(instructor_1)

# instructor_2 = Instructor("Bill", 45)
# instructor_repository.save(instructor_2)

# instructor_3 = Instructor("Paula", 66)
# instructor_repository.save(instructor_3)

# member_1 = Member("Cameron", 25, "Gold")
# member_repository.save(member_1)

# member_2 = Member("Rory", 46, "Silver")
# member_repository.save(member_2)

# member_3 = Member("Andrew", 26, "Bronze")
# member_repository.save(member_3)

workout_1 = Workout("Fuego", "HIIT", 45, "5th December 2020", 5)
workout_repository.save(workout_1)

workout_2 = Workout("Stretch", "Yoga", 70, "6th December 2020", 3)
workout_repository.save(workout_2)

workout_3 = Workout("Spin", "Cycle", 30, "7th December 2020", 15)
workout_repository.save(workout_3)

#Save function - working
#Select all function - working
#Select by id - list index out of range error

pdb.set_trace()