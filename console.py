import pdb

from models.instructor import Instructor
from models.member import Member
from models.workout import Workout

import repositories.instructor_repository as instructor_repository
# import repositories.workout_repository as workout_repository
import repositories.member_repository as member_repository

instructor_repository.delete_all()

instructor_1 = Instructor("Emily", 21)
instructor_repository.save(instructor_1)

instructor_2 = Instructor("Bill", 45)
instructor_repository.save(instructor_2)

instructor_3 = Instructor("Paula", 66)
instructor_repository.save(instructor_3)

member_1 = Member("Cameron", 25, "Gold")
