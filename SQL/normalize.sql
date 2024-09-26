create table if not exists Countries (
    country_id serial primary key,
    country_name varchar(100) unique not null
);

create table if not exists Cities (
    city_id serial primary key,
    city_name varchar(100) unique not null,
    country_id int unique not null,
    latitude decimal(10,8),
    longitude decimal(11,8),
    foreign key (country_id) references Countries(country_id)
);

create table if not exists TargetTypes (
    target_type_id serial primary key,
    target_type_name varchar(255) unique not null
);

create table if not exists Targets (
    target_id serial primary key,
    target_name varchar(255) unique not null,
    city_id int unique not null,
    target_type_id int,
    foreign key (city_id) references Cities(city_id),
    foreign key (target_type_id) references TargetTypes (target_type_id)
);