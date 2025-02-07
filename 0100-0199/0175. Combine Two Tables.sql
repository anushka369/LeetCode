SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address USING (personId);

-- Link to the problem: https://leetcode.com/problems/combine-two-tables/
