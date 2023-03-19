-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT tvg.name FROM tv_shows AS tvs
	INNER JOIN tv_show_genres AS tvsg
		ON tvs.id = tvsg.show_id
	INNER JOIN tv_genres AS tvg
		ON tvsg.genre_id = tvg.id
	WHERE tvs.title = "Dexter"
	ORDER BY tvg.name ASC;
