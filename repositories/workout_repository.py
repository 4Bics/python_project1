from db.run_sql import run_sql
from models.workout import Workout

#Create save method 
def save(workout):
  sql = "INSERT INTO workouts (name, type, duration, date, capacity) VALUES (%s, %s, %s, %s, %s) RETURNING id"
  values = [workout.name, workout.type, workout.duration, workout.date, workout.capacity]
  results = run_sql(sql, values)
  id = results[0]['id']
  workout.id = id

#Create select all method
def select_all():
  workouts = []
  sql = "SELECT * FROM workouts"
  results = run_sql(sql)
  for result in results:
    workout = Workout(result["name"], result["type"], result["duration"], result["date"], result["capacity"], result["id"])
    workouts.append(workout)
  return workouts

#Create select by id
def select(id):
  sql = "SELECT * FROM workouts WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  workout = Workout(result["name"], result["type"], result["duration"], result["date"], result["capacity"], result["id"])
  return workout

#Create delete all method
def delete_all():
  sql = "DELETE FROM workouts"
  run_sql(sql)

#Create delete by id
def delete(id):
  sql = "DELETE FROM workouts WHERE id = %s"
  values = [id]
  run_sql(sql, values)