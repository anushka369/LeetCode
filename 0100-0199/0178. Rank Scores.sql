SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores;

-- Link to the problem: https://leetcode.com/problems/rank-scores/
