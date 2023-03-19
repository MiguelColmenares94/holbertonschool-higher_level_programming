-- lists all Comedy shows in the database hbtn_0d_tvshows

SELECT tvs.title FROM tv_genres AS tvg
	INNER JOIN tv_show_genres AS tvsg
		ON tvg.id = tvsg.genre_id
	INNER JOIN tv_shows AS tvs
		ON tvsg.show_id = tvs.id
	WHERE tvg.name = "Comedy"
	ORDER BY tvs.title ASC;
