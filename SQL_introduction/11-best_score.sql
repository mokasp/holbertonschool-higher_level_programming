-- SQL script shows name and score colums where score is greater than 10 in descending order from TABLE in current DATABASE
SELECT score, name FROM `second_table`
WHERE score >= 10
ORDER BY score DESC;
