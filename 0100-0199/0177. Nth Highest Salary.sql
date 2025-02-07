CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN SET N = N - 1;
  
RETURN 
(
    SELECT 
    (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    )
);
END

-- Link to the problem: https://leetcode.com/problems/nth-highest-salary/
