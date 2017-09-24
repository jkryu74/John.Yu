#1
SELECT countries.name, languages.language
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = "Slovene";
#2
SELECT countries.name AS countries, COUNT(*) cities
FROM countries
JOIN cities ON cities.country_code = countries.code
GROUP BY countries.name
ORDER BY COUNT(*)  DESC;
#3
SELECT countries.name AS country, cities.name AS city, cities.population AS population
FROM countries 
JOIN cities ON countries.code = cities.country_code
WHERE countries.name = "Mexico"
AND cities.population > 500000
ORDER BY cities.population DESC;
#4
SELECT countries.name AS country, languages.language AS language, languages.percentage AS percentage
FROM languages
JOIN countries ON countries.code = languages.country_code
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;
#5
SELECT countries.name AS country, countries.surface_area AS size, countries.population
FROM countries
WHERE countries.surface_area < 501
AND countries.population > 100000;
#6
SELECT countries.name AS country, countries.government_form, countries.life_expectancy
FROM countries
WHERE (countries .government_form = "constitutional monarchy" OR countries.government_form = "monarchy")
AND countries.life_expectancy > 75;
#7
SELECT cities.district, cities.name, cities.population
FROM cities
JOIN countries on cities.country_code = countries.code 
WHERE countries.name = "Argentina"
AND cities.district = "Buenos Aires"
AND cities.population > 500000;

SELECT countries.continent, COUNT(*) FROM countries
GROUP BY countries.continent
ORDER BY COUNT(*) DESC;
