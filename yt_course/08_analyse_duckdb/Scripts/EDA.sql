SELECT * FROM youtube;

SELECT DISTINCT category FROM youtube;

SELECT
	count(category) AS number_is_science
FROM
	youtube
WHERE
	category = 'Science & Technology'
	
	
SELECT
	"youtuber name", category
FROM
	youtube
WHERE
	category = 'Science & Technology'
	
	
SELECT * FROM youtube;


SELECT
	*
FROM
	youtube
WHERE
	category = 'Science & Technology'
	OR category = 'Education';