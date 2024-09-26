-- כאן מופיע יעילות השאלה לפני יצירת האינדקס



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




--befor i create the index
--execute time 62.319


--after i create those index:


CREATE INDEX idx_mission_date ON mission (extract(year from mission_date));
CREATE INDEX idx_mission_id ON mission (mission_id);


"              Group Key: air_force, target_city"
"              Batches: 1  Memory Usage: 369kB"
"              ->  Bitmap Heap Scan on mission  (cost=19.33..2137.00 rows=891 width=18) (actual time=2.620..4.863 rows=23214 loops=1)"
"                    Recheck Cond: (EXTRACT(year FROM mission_date) = '1943'::numeric)"
"                    Heap Blocks: exact=949"
"                    ->  Bitmap Index Scan on idx_mission_date  (cost=0.00..19.10 rows=891 width=0) (actual time=2.513..2.514 rows=23214 loops=1)"
"                          Index Cond: (EXTRACT(year FROM mission_date) = '1943'::numeric)"
"Planning Time: 1.236 ms"
"Execution Time: 7.866 ms"

--after i create the indexes



---------------------------------------------------------------





-- כאן מופיע יעילות השאלה לפני יצירת האינדקס



EXPLAIN ANALYZE
select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1


--befor i create the index



--CREATE INDEX idx_airborne_aircraft ON mission (airborne_aircraft);
--CREATE INDEX idx_bomb_damage_assessment ON mission (bomb_damage_assessment);


"Limit  (cost=5784.50..5784.50 rows=1 width=52) (actual time=34.994..38.304 rows=1 loops=1)"
"  ->  Sort  (cost=5784.50..5784.57 rows=29 width=52) (actual time=34.993..38.302 rows=1 loops=1)"
"        Sort Key: (count(bomb_damage_assessment)) DESC"
"        Sort Method: top-N heapsort  Memory: 25kB"
"        ->  Finalize GroupAggregate  (cost=5780.79..5784.36 rows=29 width=52) (actual time=34.966..38.293 rows=21 loops=1)"
"              Group Key: target_country, bomb_damage_assessment"
"              ->  Gather Merge  (cost=5780.79..5783.83 rows=24 width=52) (actual time=34.955..38.277 rows=21 loops=1)"
"                    Workers Planned: 2"
"                    Workers Launched: 2"
"                    ->  Partial GroupAggregate  (cost=4780.76..4781.03 rows=12 width=52) (actual time=10.128..10.132 rows=7 loops=3)"
"                          Group Key: target_country, bomb_damage_assessment"
"                          ->  Sort  (cost=4780.76..4780.79 rows=12 width=36) (actual time=10.124..10.125 rows=11 loops=3)"
"                                Sort Key: target_country, bomb_damage_assessment"
"                                Sort Method: quicksort  Memory: 26kB"
"                                Worker 0:  Sort Method: quicksort  Memory: 25kB"
"                                Worker 1:  Sort Method: quicksort  Memory: 25kB"
"                                ->  Parallel Seq Scan on mission  (cost=0.00..4780.55 rows=12 width=36) (actual time=6.834..10.050 rows=11 loops=3)"
"                                      Filter: ((bomb_damage_assessment IS NOT NULL) AND (airborne_aircraft > '5'::numeric))"
"                                      Rows Removed by Filter: 59416"
"Planning Time: 0.749 ms"
"Execution Time: 38.369 ms"



--after i create those index:


"Limit  (cost=339.65..339.65 rows=1 width=52) (actual time=0.247..0.248 rows=1 loops=1)"
"  ->  Sort  (cost=339.65..339.72 rows=29 width=52) (actual time=0.247..0.247 rows=1 loops=1)"
"        Sort Key: (count(bomb_damage_assessment)) DESC"
"        Sort Method: top-N heapsort  Memory: 25kB"
"        ->  GroupAggregate  (cost=338.85..339.51 rows=29 width=52) (actual time=0.233..0.241 rows=21 loops=1)"
"              Group Key: target_country, bomb_damage_assessment"
"              ->  Sort  (cost=338.85..338.93 rows=29 width=36) (actual time=0.229..0.230 rows=32 loops=1)"
"                    Sort Key: target_country, bomb_damage_assessment"
"                    Sort Method: quicksort  Memory: 26kB"
"                    ->  Bitmap Heap Scan on mission  (cost=5.01..338.15 rows=29 width=36) (actual time=0.134..0.195 rows=32 loops=1)"
"                          Recheck Cond: (bomb_damage_assessment IS NOT NULL)"
"                          Filter: (airborne_aircraft > '5'::numeric)"
"                          Rows Removed by Filter: 72"
"                          Heap Blocks: exact=53"
"                          ->  Bitmap Index Scan on idx_bomb_damage_assessment  (cost=0.00..5.01 rows=95 width=0) (actual time=0.117..0.117 rows=104 loops=1)"
"                                Index Cond: (bomb_damage_assessment IS NOT NULL)"
"Planning Time: 1.747 ms"
"Execution Time: 0.276 ms"



--CREATE INDEX idx_mission_date ON mission (extract(year from mission_date));
--CREATE INDEX idx_airborne_aircraft ON mission (airborne_aircraft);
--CREATE INDEX idx_bomb_damage_assessment ON mission (bomb_damage_assessment);
--CREATE INDEX idx_mission_id ON mission (mission_id);

בחרתי באינדקסים האלה כי הם הכי היו יעילים לפרויקט
ולביצוע השאילתות זה מסייע גם זמן הביצוע
וכן זה יעזור גם לשאילתות עתידיות כך שזה יכןל להיות גנרי
