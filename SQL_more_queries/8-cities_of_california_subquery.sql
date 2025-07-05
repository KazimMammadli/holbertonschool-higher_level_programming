-- Cities of California
USE hbtn_0d_usa;
SELECT id, state_id, name FROM cities where state_id = ( SELECT id FROM states WHERE name = 'California') ORDER BY id ASC ;
