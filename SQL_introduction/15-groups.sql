-- SQL script that lists number of records with same score in TABLE
SELECT
    score,
    COUNT(score)
FROM
    `second_table`
GROUP BY
    score;
