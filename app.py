from flask import Flask
from controllers.targets_controller import target_blueprint
from repository.target_repository import get_all_targets

app = Flask(__name__)


if __name__ == '__main__':
    app.register_blueprint(target_blueprint, url_prefix='/api/targets')

    app.run(debug=True)