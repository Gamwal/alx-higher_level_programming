-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tg.name, SUM(tsr.rate) rating
FROM tv_shows ts
	INNER JOIN tv_show_ratings tsr
	ON ts.id = tsr.show_id
	INNER JOIN tv_show_genres tsg
	ON tsr.show_id = tsg.show_id
	INNER JOIN tv_genres tg
	ON tsg.genre_id = tg.id
GROUP BY tg.name
ORDER BY rating DESC;
