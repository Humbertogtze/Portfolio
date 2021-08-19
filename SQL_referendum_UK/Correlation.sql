-- In this query, I will demonstrate any correlation between population and age in how populations voted in the 2016 UK Brexit

--Create a temp table with the relevant data, and joins the two tables

DROP TABLE IF exists #PopAndVotes

CREATE TABLE #PopAndVotes(
Type nvarchar(255),
[Area Name] nvarchar(255),
All_residents int,
Age_0_to_4 int,
Age_5_to_9 int,
Age_10_to_14 int,
Age_15_to_19 int,
Age_20_to_24 int,
Age_25_to_29 int,
Age_30_to_34 int,
Age_35_to_39 int,
Age_40_to_44 int,
Age_45_to_49 int,
Age_50_to_54 int,
Age_55_to_59 int,
Age_60_to_64 int,
Age_65_to_69 int,
Age_70_to_74 int,
Age_75_to_79 int,
Age_80_to_84 int,
Age_85_to_89 int,
Age_90_and_over int,
Valid_votes int,
Remain int,
Leave int,
[Land Area] float
)

INSERT INTO #PopAndVotes
SELECT cen.Type, cen.Area, cen.[All Residents], cen.[Age 0 to 4], cen.[Age 5 to 9], cen.[Age 10 to 14], cen.[Age 15 to 19], cen.[Age 20 to 24]
, cen.[Age 25 to 29], cen.[Age 30 to 34], cen.[Age 35 to 39], cen.[Age 40 to 44], cen.[Age 45 to 49], cen.[Age 50 to 54], cen.[Age 55 to 59]
,cen.[Age 60 to 64], cen.[Age 65 to 69], cen.[Age 70 to 74], cen.[Age 75 to 79], cen.[Age 80 to 84], cen.[Age 85 to 89], cen.[Age 90 and Over]
, ref.[Valid Votes], ref.Remain, ref.Leave, area.AREALHECT
FROM portfolio..census cen 
INNER JOIN portfolio..referendum$ ref
	ON cen.Code = ref.[Area Code]
LEFT JOIN Portfolio..AreaPerDistrict area
	ON cen.Code = area.LAD16CD
ORDER BY Type

SELECT *
FROM #PopAndVotes

/* 
This data itself was very clean, but there are still some issues, primarely with Scotland and Northern Ireland.
With Scotland, they seemed to round up the values on their population, which is not catastrophic. But the main problem is that there
are a couple of Null values.
With Northen Ireland the problem is a little more complex. There is no data for Northern Ireland districts in the referendum,
there is only data for it as a country. Luckily, we have data for it as a country in the census, but not in the area dataset.
*/

--Replaces the null values with 0s

UPDATE #PopAndVotes 
SET Age_85_to_89 = 0
WHERE Age_85_to_89 IS NULL

UPDATE #PopAndVotes 
SET Age_90_and_over = 0
WHERE Age_90_and_over IS NULL

--Now I get the comulative sum to get mean age

WITH Freq (Area, Sum, Population)
AS
(
SELECT Area, SUM(Age_0_to_4*2 + Age_5_to_9*7 + Age_10_to_14*12 + Age_15_to_19*17 + Age_20_to_24*22 + Age_25_to_29*27
+ Age_30_to_34*32 + Age_35_to_39*37 + Age_40_to_44*42 + Age_45_to_49*47 + Age_50_to_54*52 + Age_55_to_59*57 + Age_60_to_64*62
+ Age_65_to_69*67 + Age_70_to_74*72 + Age_75_to_79*77 + Age_80_to_84*82 + Age_85_to_89*87 + Age_90_and_over*90) AS Cummulative
,All_residents
FROM #PopAndVotes
GROUP BY Area, All_residents
)
SELECT Area, Sum/Population AS [Average age]
FROM Freq
ORDER BY [Average age]



