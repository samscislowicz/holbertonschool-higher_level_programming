-- A script that creates the database hbtn_0d_usa
-- If the database hbtn_0d_usa already exists your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT PRIMARY KEY AUTO_INCREMENT, state_id INT, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id), name VARCHAR(256) NOT NULL);
