-- a script that lists all the cities of California
-- Results must be sorted in ascending order by cities.id
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
