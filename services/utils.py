from models.Targets import targets



def target_to_json(target: targets) -> dict:
    return {
        "target_id": target.target_id,
        "target_industry": target.target_industry,
        "city_id": target.city_id,
        "target_type_id": target.target_type_id,
        "target_priority": target.target_priority
    }
