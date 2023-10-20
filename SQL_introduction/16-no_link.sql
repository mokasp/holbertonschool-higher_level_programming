-- SQL script that lists all records of TABLE in which name is not NULL
SELECT score, name FROM `second_table`
WHERE
    name IS NOT NULL
ORDER BY
    score DESC;
