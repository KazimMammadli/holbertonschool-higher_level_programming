-- Temperatures #1
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = "July" or month = "August" 
GROUP BY city 
ORDER BY AVG(value) DESC
LIMIT 3;
