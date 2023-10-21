-- SQL script CREATES a table with a column where null is not allowed
CREATE TABLE IF NOT EXISTS `force_name` (
    id INT,
    name VARCHAR(256) NOT NULL
);
