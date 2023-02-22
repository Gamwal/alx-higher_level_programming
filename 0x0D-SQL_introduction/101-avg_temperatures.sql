-- sql to display temperature by city by temperature descending
SELECT city, AVG(value) AS 'avg_temp' 
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
