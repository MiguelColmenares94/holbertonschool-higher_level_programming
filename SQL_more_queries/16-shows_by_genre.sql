-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows

SELECT tvs.title, tvg.name FROM tv_genres AS tvg
	INNER JOIN tv_show_genres AS tvsg
		ON tvg.id = tvsg.genre_id
	RIGHT JOIN tv_shows AS tvs
		ON tvsg.show_id = tvs.id
	ORDER BY tvs.title ASC, tvg.name ASC;
