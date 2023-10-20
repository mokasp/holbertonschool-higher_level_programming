-- SQL script that lists number of records with same score in TABLE
SELECT
    score,
    COUNT(score)
AS
    number
FROM
    `second_table`
GROUP BY
    score
ORDER BY
    score DESC;
