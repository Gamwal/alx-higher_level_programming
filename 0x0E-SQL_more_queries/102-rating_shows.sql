-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT ts.title, SUM(tsr.rate) rating
FROM tv_shows ts
	INNER JOIN tv_show_ratings tsr
	ON ts.id = tsr.show_id
GROUP BY ts.title
ORDER BY rating DESC;
