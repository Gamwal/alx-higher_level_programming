-- sql script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT DISTINCT cities FROM states
WHERE states = 'California'
ORDER BY id ASC;
