from db.run_sql import run_sql
from models.member import Member

#Create save method 
def save(member):
  sql = "INSERT INTO members (name, age, membership_type) VALUES (%s, %s, %s) RETURNING id"
  values = [member.name, member.age, member.membership_type]
  results = run_sql(sql, values)
  id = results[0]['id']
  member.id = id

#Create select all method
def select_all():
  members = []
  sql = "SELECT * FROM members"
  results = run_sql(sql)
  for result in results:
    member = Member(result["name"], result["age"], result["membership_type"], result["id"])
    members.append(member)
  return members

#Create select by id
def select(id):
  sql = "SELECT * FROM members WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  member = Member(result["name"], result["age"], result["membership_type"], result["id"])
  return member 

#Create delete all method
def delete_all():
  sql = "DELETE FROM members"
  run_sql(sql)

#Create delete by id
def delete(id):
  sql = "DELETE FROM members WHERE id = %s"
  values = [id]
  run_sql(sql, values)

#Create update by id
def update(member):
  sql = "UPDATE members SET (name, age, membership_type) = (%s, %s, %s) WHERE id = %s"
  values = [member.name, member.age, member.membership_type, member.id]
  run_sql(sql, values)