from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.workout_repository as workout_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

#Index
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

#New booking
@bookings_blueprint.route("/bookings/book", methods = ['GET'])
def new_booking():
  workouts = workout_repository.select_all()
  members = member_repository.select_all()
  return render_template("bookings/book.html", workouts = workouts, members = members)

@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
  workout_id = request.form["workout_id"]
  member_id = request.form["member_id"]
  workout = workout_repository.select(workout_id)
  member = member_repository.select(member_id)
  new_booking = Booking(workout, member)
  booking_repository.save(new_booking)
  return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
  booking = booking_repository.select(id)
  workouts = workout_repository.select_all()
  members = member_repository.select_all()
  return render_template("/bookings/edit.html", booking=booking, workouts=workouts, members=members)

@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
  workout_id = request.form["workout_id"]
  member_id = request.form["member_id"]
  workout = workout_repository.select(workout_id)
  member = member_repository.select(member_id)
  booking = Booking(workout, member, id)
  booking_repository.update(booking)
  return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")
