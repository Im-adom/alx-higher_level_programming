-- lists all privileges of the MySQL users user_0d_1 and
-- user_0d_2 on your server (in localhost)
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
