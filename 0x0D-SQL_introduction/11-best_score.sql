-- sql script to list all records with score >= 10 of second_table in hbtn_0c_0 DB
SELECT score, name FROM second_table WHERE score >=10 ORDER BY score DESC;
