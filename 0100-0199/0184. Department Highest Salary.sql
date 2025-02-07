SELECT d.name AS department, 
       e.name AS employee, 
       salary
  
FROM Employee AS e
JOIN Department AS d 
ON e.departmentId = d.id
  
WHERE (d.id, salary) IN 
(
    SELECT departmentId, MAX(salary)
    FROM Employee GROUP BY 1
);

-- Link to the problem: https://leetcode.com/problems/department-highest-salary/
