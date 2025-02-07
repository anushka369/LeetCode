SELECT w1.id FROM Weather AS w1
JOIN Weather AS w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 
AND w1.temperature > w2.temperature;

-- Link to the problem: https://leetcode.com/problems/rising-temperature/
