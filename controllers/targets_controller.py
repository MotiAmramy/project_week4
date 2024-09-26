from flask import Blueprint, request, jsonify
from returns.result import Success
from repository.target_repository import insert_target, find_target_by_id, update_target, delete_target_by_id, get_all_targets
from models.Targets import targets
from services.utils import target_to_json


target_blueprint = Blueprint("targets", __name__)

@target_blueprint.route("/", methods=['GET'])
def get_targets():
    targets = get_all_targets()
    target_list = [
        {
            "target_id": target.target_id,
            "target_industry": target.target_industry,
            "city_id": target.city_id,
            "target_type_id": target.target_type_id,
            "target_priority": target.target_priority
        }
        for target in targets
    ]
    return jsonify(target_list), 200


@target_blueprint.route("/create", methods=['POST'])
def create_target():
    data = request.json
    target = targets(
        target_industry=data.get("target_industry"),
        city_id=data.get("city_id"),
        target_type_id=data.get("target_type_id"),
        target_priority=data.get("target_priority")
    )

    result = insert_target(target)
    if isinstance(result, Success):
        return jsonify(target_to_json(result.unwrap())), 201
    else:
        return jsonify({"error": result.error}), 400


@target_blueprint.route("/<int:target_id>", methods=['GET'])
def get_target(target_id: int):
    return (
        find_target_by_id(target_id)
        .map(target_to_json)
        .map(lambda t: (jsonify(t), 200))
        .value_or((jsonify({"error": "Target not found"}), 404))
    )


@target_blueprint.route("/<int:target_id>", methods=['PUT'])
def update_target_route(target_id: int):
    data = request.json
    target = Targets(
        target_industry=data.get("target_industry"),
        city_id=data.get("city_id"),
        target_type_id=data.get("target_type_id"),
        target_priority=data.get("target_priority")
    )
    result = update_target(target_id, target)
    if isinstance(result, Success):
        return jsonify(target_to_json(result.value)), 200
    else:
        return jsonify({"error": result.error}), 400


@target_blueprint.route("/<int:target_id>", methods=['DELETE'])
def delete_target(target_id: int):
    result = delete_target_by_id(target_id)
    if isinstance(result, Success):
        return jsonify(target_to_json(result.value)), 200
    else:
        return jsonify({"error": result.error}), 404


