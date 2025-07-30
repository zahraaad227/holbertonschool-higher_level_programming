-- sql
SELECT city.id, city.name, states.name
FROM cities, states
WHERE cities.state_id = state.id
ORDER BY city.id ASC;
