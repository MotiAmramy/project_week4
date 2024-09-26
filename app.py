from flask import Flask

from controllers.mission_controller import mission_blueprint
from controllers.targets_controller import target_blueprint

app = Flask(__name__)


if __name__ == '__main__':
    app.register_blueprint(target_blueprint, url_prefix='/api/targets')
    app.register_blueprint(mission_blueprint, url_prefix='/api/missions')
    app.run(debug=True)