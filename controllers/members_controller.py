from flask import Blueprint, Flask, redirect, render_template, render_template, request

from models.member import Member
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
  members = member_repository.select_all()
  return render_template("members/index.html", members = members)

@members_blueprint.route("/members/new", methods = ['GET'])
def new_member():
  members = member_repository.select_all()
  workouts = workout_repository.select_all()
  return render_template("members/new.html", members = members, workouts=workouts)

@members_blueprint.route("/members", methods=['POST'])
def create_member():
  name = request.form['name']
  age = request.form['age']
  membership_type = request.form['membership_type']
  # enrolled_class = member_repository.select(request.form['workout.id'])
  enrolled_class = request.form['enrolled_class']
  member = Member(name, age, membership_type, enrolled_class)
  member_repository.save(member)
  return redirect('/members')
