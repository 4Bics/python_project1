from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.workout_repository as workout_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings/book", methods = ['GET'])
def new_booking():
  workouts = workout_repository.select_all()
  members = member_repository.select_all()
  return render_template("workouts/book.html", workouts = workouts, members = members)

# @workouts_blueprint.route("/workouts", methods = ['POST'])
# def create_booking():
