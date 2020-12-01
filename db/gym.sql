DROP TABLE IF EXISTS workouts;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS instructors;

CREATE TABLE workouts (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  type VARCHAR(255),
  duration INT,
  date VARCHAR(255),
  capacity INT,
  instructor_id INT REFERENCES instructors(id) ON DELETE CASCADE,
  member_id INT REFERENCES members(id) ON DELETE CASCADE
);

CREATE TABLE instructors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  age INT
);

CREATE TABLE members (
  id SERIAL PRIMARY KEY,
  age INT, 
  membership_type VARCHAR(255)
);