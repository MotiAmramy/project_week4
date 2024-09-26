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
