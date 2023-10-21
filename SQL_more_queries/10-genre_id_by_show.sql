-- SQL script that joins tv show titles with the id of their genres (left join)
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
    LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
