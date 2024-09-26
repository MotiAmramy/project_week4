## Targets API
## fetch one

```python
from config.base import session_factory
from sqlalchemy import text
from models import Target

with session_factory() as session:
    selection_result = session.execute(text("select * from targets where city_id = :city_id"), {"city_id": 1})
    target_dict = selection_result.fetchone()
    target = Target(
        city_id=target_dict["city_id"],
        target_industry=target_dict["target_industry"],
        target_type_id=target_dict["target_type_id"],
        target_priority=target_dict["target_priority"]
    )
```

## fetch all
```python
from config.base import session_factory
from sqlalchemy import text
from models import Target

with session_factory() as session:
    selection_result = session.execute(text("select * from targets"), {})
    targets_dict = selection_result.fetchall()
    targets = [
        Target(
            city_id=target[0],
            target_industry=target[1],
            target_type_id=target[2],
            target_priority=target[3]
        )
        for target in targets_dict
    ]
```

## delete

```python
from config.base import session_factory
from sqlalchemy import text
from models import Target

with session_factory() as session:
    target = session.get(Target, t_id)
    if target:
        session.delete(target)
        session.commit()
        
```



#### group by count of quote only when the 
#### results of the group by is greater than 1

```sql
select count(m.air_force), m.air_force, m.target_city from mission as m
where extract(year from mission_date) = 1943
group by m.air_force, m.target_city
order by count(m.target_city) desc
limit 1
```

### subqueries

```sql
select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc

```

### create index
```sql**
CREATE INDEX idx_mission_date ON mission (extract(year from mission_date));
CREATE INDEX idx_airborne_aircraft ON mission (airborne_aircraft);
CREATE INDEX idx_bomb_damage_assessment ON mission (bomb_damage_assessment);
CREATE INDEX idx_mission_id ON mission (mission_id);**
```

### check this out!!
```sql
create index city_idx_developer_city_id on developer_companies(developer_city_id)
```

```sql
explain analyze select * from ...
```