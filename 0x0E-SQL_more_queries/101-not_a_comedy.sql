-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT ts.title 
FROM tv_shows ts
WHERE ts.title NOT IN 
	(SELECT title
	FROM tv_shows
		INNER JOIN tv_show_genres tsg
	        ON ts.id = tsg.show_id
		INNER JOIN tv_genres tg
        	ON tsg.genre_id = tg.id	
		WHERE tg.name = 'Comedy')
ORDER BY ts.title ASC;
