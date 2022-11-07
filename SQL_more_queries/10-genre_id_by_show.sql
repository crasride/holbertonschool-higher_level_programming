-- Import the database dump from hbtn_0d_tvshows
-- (cat hbtn_0d_tvshows\.sql | sudo mysql -uroot -p hbtn_0d_tvshows)
-- lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
