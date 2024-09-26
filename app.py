from flask import Flask
from controllers.targets_controller import target_blueprint
from repository.target_repository import get_all_targets

app = Flask(__name__)


if __name__ == '__main__':
    app.register_blueprint(target_blueprint, url_prefix='/api/targets')

    a = get_all_targets()
    target_list = [
        {
            "target_id": target.target_id,
            "target_industry": target.target_industry,
            "city_id": target.city_id,
            "target_type_id": target.target_type_id,
            "target_priority": target.target_priority
        }
        for target in a
    ]
    # print(target_list)
    app.run(debug=True)