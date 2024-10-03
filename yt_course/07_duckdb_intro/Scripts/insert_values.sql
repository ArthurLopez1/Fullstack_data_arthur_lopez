CREATE TABLE jokes (id INTEGER PRIMARY KEY,
joke_text VARCHAR,
rating INTEGER);

desc;

INSERT
	INTO
	jokes (id,
	joke_text,
	rating)
VALUES
(1,
'Why don’t scientists trust atoms? Because they make up everything!',
8),
(2,
'Why did the scarecrow win an award? Because he was outstanding in his field!',
7),
(3,
'I told my wife she was drawing her eyebrows too high. She looked surprised.',
9),
(4,
'Why don’t skeletons fight each other? They don’t have the guts.',
6);


SELECT * FROM jokes;


SELECT * FROM jokes WHERE rating > 6;

DESC jokes;


INSERT
	INTO
	jokes (id,
	joke_text,
	rating)
VALUES (5,
'Why some couples dont go to the gym? Because some relationships dont workout.',
8),
(6,
'I would avoid the sushi if I was was you. Its a little fishy.',
7),
(7,
'Why dont programmers like nature? It has too many bugs',
9),
(8, 'Wanna hear a joke about construction? Im still working on it', 6),
(9,
'How does a penguin build its house? Igloos it together.',
1),
(10,
'A gothenburg person stands in queue for star wars when someone cuts the line he says ge daj.',
2);

SELECT * FROM jokes;