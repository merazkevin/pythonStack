SELECT * FROM world.cities;
#1. What query would you run to get all the countries that speak Slovene? Your query 
#should return the name of the country, language and language percentage. Your query 
#should arrange the result by language percentage in descending order. (1)
SELECT * FROM world.countrylanguage WHERE world.countrylanguage.Language='slovene';
SELECT * FROM world.countrylanguage WHERE world.countrylanguage.Language='slovene' AND IsOfficial=TRUE;

#2. What query would you run to display the total number of cities for each country? 
#Your query should return the name of the country and the total number of cities. 
#Your query should arrange the result by the number of cities in descending order. (3)
SELECT * FROM world.countries; 
select * from world.countries where world.countries.id ORDER BY id DESC;

#3. What query would you run to get all the cities in Mexico with a population of greater
# than 500,000? Your query should arrange the result by population in descending order. (1)

SELECT countries.name, cities.name, cities.population
FROM world.countries
JOIN  cities 
ON countries.id = cities.country_id 
WHERE countries.name='Mexico'and cities.population>='500000'
ORDER BY  cities.population DESC;

#4. What query would you run to get all languages
# OF ONLY in each country with a percentage greater than 89%? 
#Your query should arrange the result by percentage in descending order. (1)
SELECT countries.name, languages.language, languages.percentage
FROM world.countries
JOIN languages ON countries.id = languages.country_id 
WHERE languages.percentage>='89'ORDER BY languages.percentage DESC; 

#5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
SELECT countries.name, countries.surface_area 
FROM world.countries WHERE surface_area < 501 ORDER BY surface_area;

#6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 
#and a life expectancy greater than 75 years? (1)
SELECT countries.name, countries.government_form, 
countries.capital, countries.life_expectancy
FROM world.countries WHERE countries.capital>200  and countries.government_form='Constitutional Monarchy' 
and life_expectancy>75 ORDER BY life_expectancy DESC;

#7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the 
#population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)
SELECT cities.name, cities.district, cities.country_code 
FROM world.cities WHERE cities.country_code = 'ARG'
AND cities.district = 'Buenos Aires';

#8. What query would you run to summarize the number of countries in each region? The query should display the name 
#of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)
 SELECT countries.name, countries.region
 FROM world.countries ORDER BY countries.region;
#Note: You may download this PDF file displaying the expected results from the queries

>;P