DELETE FROM Person
WHERE id NOT IN 
(
    SELECT MIN(id) 
    FROM (SELECT * FROM Person)
    AS p GROUP BY email
);

-- Link to the problem: https://leetcode.com/problems/delete-duplicate-emails/
