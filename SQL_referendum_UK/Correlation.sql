-- In this query, I will demonstrate any correlation between population and age in how populations voted in the 2016 UK Brexit

--Joins the two table by the Area name.

SELECT *
FROM portfolio..census cen
INNER JOIN portfolio..referendum$ ref
	ON cen.Area = ref.Area
ORDER BY Type

/* 
It is important to point out that the Area name must be used instead of area codes due to some funkiness in how these codes
are established, it is just more optimal. For example, Northern Ireland is included in the census as multiple districts,
but only as a country in the Referendum
*/



