from flask import Blueprint, Flask, redirect, render_template, render_template, request

from models.workout import Workout
import repositories.workout_repository as workout_repository
import repositories.member_repository as member_repository

workouts_blueprint = Blueprint("workouts", __name__)

@workouts_blueprint.route("/workouts")
def workouts():
  workouts = workout_repository.select_all()
  return render_template("workouts/index.html", workouts = workouts)

@workouts_blueprint.route("/workouts/<id>")
def show(id):
  workout = workout_repository.select(id)
  return render_template("workouts/show.html", workout = workout)

@workouts_blueprint.route("/workouts/book", methods = ['GET'])
def new_booking():
  workouts = workout_repository.select_all()
  members = member_repository.select_all()
  return render_template("workouts/book.html", workouts = workouts, members = members)

# @workouts_blueprint.route("/workouts", methods = ['POST'])
# def create_booking():

@workouts_blueprint.route("/workout/new", methods = ['GET'])
def new_workout():
  workouts = workout_repository.select_all()
  return render_template("members/new.html", workouts=workouts)

@workouts_blueprint.route("/workouts", methods=['POST'])
def create_workout():
  name = request.form['name']
  type = request.form['type']
  duration = request.form['duration']
  date = request.form['date']
  capacity = request.form['capacity']
  workout = Workout(name, type, duration, date, capacity)
  workout_repository.save(workout)
  return redirect('/workouts')

