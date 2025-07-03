-- Average
ALTER TABLE second_table ADD COLUMN average DECIMAL(10, 2)
INSERT INTO second_table(average) SELECT AVG(score) FROM second_table;

