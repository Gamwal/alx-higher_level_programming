-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT ts.title, tg.genre_id
FROM tv_shows ts LEFT OUTER JOIN tv_show_genres tg
ON ts.id = tg.show_id
WHERE tg.show_id IS NULL
ORDER BY ts.title ASC, tg.genre_id ASC;
