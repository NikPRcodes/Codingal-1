SELECT MAX(Win_Margin), MIN(Win_Margin) 
FROM Match;

SELECT * FROM Team
WHERE Team_Name LIKE 'De%';

SELECT * FROM Match
WHERE Match_Winner ==7 AND Season_Id IN (8,9);