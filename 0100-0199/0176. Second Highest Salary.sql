SELECT
(
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1, 1
) 
AS SecondHighestSalary;

-- Link to the problem: https://leetcode.com/problems/second-highest-salary/
