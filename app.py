from flask import Flask
from controllers.mission_controller import mission_blueprint
from controllers.targets_controller import target_blueprint
from native_sql import insert_data
from repository.database import create_tables
from repository.target_repository import insert_target

app = Flask(__name__)




if __name__ == '__main__':
    app.register_blueprint(target_blueprint, url_prefix='/api/targets')
    app.register_blueprint(mission_blueprint, url_prefix='/api/missions')
    create_tables()
    insert_data()
    app.run(debug=True)