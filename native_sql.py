from sqlalchemy import text
from config.base import session_factory


def create_tables():
    create_countries_table = """
    CREATE TABLE IF NOT EXISTS Countries (
        country_id SERIAL PRIMARY KEY,
        country_name VARCHAR(100) UNIQUE NOT NULL
    );
    """

    create_cities_table = """
    CREATE TABLE IF NOT EXISTS Cities (
        city_id SERIAL PRIMARY KEY,
        city_name VARCHAR(100) UNIQUE NOT NULL,
        country_id INT UNIQUE NOT NULL,
        latitude DECIMAL(10, 8),
        longitude DECIMAL(11, 8),
        FOREIGN KEY (country_id) REFERENCES Countries(country_id)
    );
    """

    create_target_types_table = """
    CREATE TABLE IF NOT EXISTS TargetTypes (
        target_type_id SERIAL PRIMARY KEY,
        target_type_name VARCHAR(255) UNIQUE NOT NULL
    );
    """

    create_targets_table = """
    CREATE TABLE IF NOT EXISTS Targets (
        target_id SERIAL PRIMARY KEY,
        target_name VARCHAR(255) UNIQUE NOT NULL,
        city_id INT UNIQUE NOT NULL,
        target_type_id INT,
        FOREIGN KEY (city_id) REFERENCES Cities(city_id),
        FOREIGN KEY (target_type_id) REFERENCES TargetTypes(target_type_id)
    );
    """

    with session_factory() as session:
        session.execute(text(create_countries_table))
        session.execute(text(create_cities_table))
        session.execute(text(create_target_types_table))
        session.execute(text(create_targets_table))
        session.commit()


def insert_data():
    insert_countries = """
    INSERT INTO Countries (country_name)
    SELECT DISTINCT target_country
    FROM mission
    WHERE target_country IS NOT NULL
    ON CONFLICT (country_name) DO NOTHING;
    """

    insert_cities = """
    INSERT INTO Cities (city_name, country_id, latitude, longitude)
    SELECT DISTINCT
        m.target_city,
        c.country_id,
        m.target_latitude::decimal,
        m.target_longitude::decimal
    FROM mission m
    JOIN Countries c ON m.country = c.country_name
    WHERE m.target_city IS NOT NULL
    ON CONFLICT (city_name) DO NOTHING;
    """

    insert_target_types = """
    INSERT INTO TargetTypes (target_type_name)
    SELECT DISTINCT target_type
    FROM mission
    WHERE target_type IS NOT NULL
    ON CONFLICT (target_type_name) DO NOTHING;
    """

    insert_targets = """
    INSERT INTO Targets (target_industry, target_priority, city_id, target_type_id)
    SELECT DISTINCT
        m.target_industry,
        m.target_priority::integer,
        ci.city_id,
        tt.target_type_id
    FROM mission m
    INNER JOIN Cities ci ON m.target_city = ci.city_name
    INNER JOIN TargetTypes tt ON m.target_type = tt.target_type_name
    WHERE m.target_id IS NOT NULL AND m.target_industry IS NOT NULL
    ON CONFLICT (target_id) DO NOTHING;
    """

    with session_factory() as session:
        session.execute(text(insert_countries))
        session.execute(text(insert_cities))
        session.execute(text(insert_target_types))
        session.execute(text(insert_targets))
        session.commit()