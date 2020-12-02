import pdb

from models.instructor import Instructor
from models.member import Member
from models.workout import Workout
from models.booking import Booking

import repositories.workout_repository as workout_repository
import repositories.member_repository as member_repository
import repositories.instructor_repository as instructor_repository

workout_repository.delete_all()
instructor_repository.delete_all()
member_repository.delete_all()

#Default Instructors 
instructor_1 = Instructor("Fran", 44, "Fuego")
instructor_repository.save(instructor_1)

instructor_2 = Instructor("White Goodman", 45, "Stretch")
instructor_repository.save(instructor_2)

instructor_3 = Instructor("Me'Shell Jones", 35, "Spin")
instructor_repository.save(instructor_3)

instructor_test = instructor_repository.select_all()
print(instructor_test[0].name)

#INSTRUCTOR_REPOSITORY
#Save function - working
#Select all function - working
#Select by id function - working
#Delete all functon - working
#Delete by id function - working
#Update function - working

#Default Members
member_1 = Member("Cameron", 25, "Gold")
member_repository.save(member_1)

member_2 = Member("Rory", 46, "Silver")
member_repository.save(member_2)

member_3 = Member("Andrew", 26, "Bronze")
member_repository.save(member_3)

member_test = member_repository.select_all()
print(member_test[1].name)

#MEMBER_REPOSITORY
#Save function - working
#Select all function - working
#Select by id function - working
#Delete all functon - working
#Delete by id function - working
#Update function - working

#Default Workouts
workout_1 = Workout("Fuego", "HIIT", 45, "5th December 2020", 5)
workout_repository.save(workout_1)

workout_2 = Workout("Stretch", "Yoga", 70, "6th December 2020", 3)
workout_repository.save(workout_2)

workout_3 = Workout("Spin", "Cycle", 30, "7th December 2020", 15)
workout_repository.save(workout_3)

workout_test = workout_repository.select_all()
print(workout_test[2].name)

#WORKOUT_REPOSITORY
#Save function - working
#Select all function - working
#Select by id function - working
#Delete all functon - working
#Delete by id function - working
#Update function - working

#Default Bookings
booking_1 = Booking(workout_1, member_1)
booking_2 = Booking(workout_2, member_2)
booking_3 = Booking(workout_3, member_3)

pdb.set_trace()