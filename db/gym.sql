DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS workouts;

CREATE TABLE workouts (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  type VARCHAR(255),
  duration INT,
  date VARCHAR(255),
  capacity INT
);

CREATE TABLE instructors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  age INT,
  workout VARCHAR(255),
  workout_id INT REFERENCES workouts(id)
);

CREATE TABLE members (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  age INT, 
  membership_type VARCHAR(255),
  enrolled_class VARCHAR(255),
  workout_id INT REFERENCES workouts(id)
);
