-- sql script that lists the number of db on mysql server
SELECT table_name
FROM information_schema.tables
WHERE table_type='BASE TABLE';
