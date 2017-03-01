-- a script that lists all cities contained in the database hbtn_0d_usa
-- You can use only one SELECT statement
SELECT DISTINCT cities.id, cities.name, states.name FROM states JOIN cities WHERE cities.state_id = states.id ORDER BY cities.id ASC;
