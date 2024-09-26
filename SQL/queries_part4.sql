SELECT 
    air_force, 
    COUNT(mission_id) AS total_missions
FROM 
    mission
WHERE 
    EXTRACT(YEAR FROM Mission_date) = 1943
GROUP BY 
    Air_force, Target_City
ORDER BY 
    total_missions DESC
LIMIT 1;

EXPLAIN
SELECT 
    air_force, 
    COUNT(mission_id) AS total_missions
FROM 
    mission
WHERE 
    EXTRACT(YEAR FROM Mission_date) = 1943
GROUP BY 
    Air_force, Target_City
ORDER BY 
    total_missions DESC
LIMIT 1;


EXPLAIN ANALYZE 
SELECT 
    air_force, 
    COUNT(mission_id) AS total_missions
FROM 
    mission
WHERE 
    EXTRACT(YEAR FROM Mission_date) = 1943
GROUP BY 
    Air_force, Target_City
ORDER BY 
    total_missions DESC
LIMIT 1;





select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1


EXPLAIN
select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1




EXPLAIN ANALYZE
select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1