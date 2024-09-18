SELECT * from youtube;

SELECT DISTINCT(category) FROM youtube;

SELECT COUNT(*) FROM youtube;

-- how many in each category TOP 10?

SELECT
	CATEGORY,
	COUNT(*) AS Quantity
FROM
	youtube
GROUP bY
	category
ORDER BY
	Quantity DESC
LIMIT 10;