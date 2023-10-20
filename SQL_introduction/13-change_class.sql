-- SQL script that deletes any record of entries with a score less than or equal to 5 from TABLE in current DATABASE
DELETE
    FROM `second_table`
WHERE 
    score <= 5;
