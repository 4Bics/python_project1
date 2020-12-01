from db.run_sql import run_sql
from models.instructor import Instructor

#Create save method 
def save(instructor):
  sql = "INSERT INTO instructors (name, age) VALUES (%s, %s) RETURNING id"
  values = [instructor.name, instructor.age]
  results = run_sql(sql, values)
  id = results[0]['id']
  instructor.id = id

#Create select all method
def select_all():
  instructors = []
  sql = "SELECT * FROM instructors"
  results = run_sql(sql)
  for result in results:
    instructor = Instructor(result["name"], result["age"], result["id"])
    instructors.append(instructor)
  return instructors

#Create select by id
def select(id):
  sql = "SELECT * FROM instructors WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  instructor = Instructor(result["name"], result["age"], result["id"])
  return instructor

#Create delete all method
def delete_all():
  sql = "DELETE FROM instructors"
  run_sql(sql)


