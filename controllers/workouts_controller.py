from flask import Blueprint, Flask, redirect, render_template, render_template, request

from models.workout import Workout
import repositories.workout_repository as workout_repository

workouts_blueprint = Blueprint("workouts", __name__)

