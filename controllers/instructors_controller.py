from flask import Blueprint, Flask, redirect, render_template, render_template, request

from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

instructors_blueprint = Blueprint("instructors", __name__)

@instructors_blueprint.route("/instructors")
def instructors():
  instructors = instructor_repository.select_all()
  return render_template("instructors/index.html", instructors = instructors)

