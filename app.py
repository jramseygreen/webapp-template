import sys
import os

from backend.server import Server
from backend.api import api
from backend.composables.response import response
from backend.composables.setup import setup_jwt, setup_db, setup_request_handling, run_migrations

def create_app(server: Server = Server()):
    app = server.get_app()
    # Can also use setter functions
    # server.set_host('localhost')
    # server.set_port(8080)
    # server.set_spa_path('frontend/dist')
    # server.set_index_file('index.html')


    api_base_url = '/api'

    server.register_blueprint(api, api_base_url)  # add a blueprint containing routes


    # add a custom 404 method, fires when given route is request prefix
    @server.errorhandler(api_base_url, 404)
    def not_found(e):
        return response.not_found('Resource not found')

    setup_db(app)
    # only run if app was launched from main - don't run when creating migrations or whatever
    if not sys.argv[0].endswith(os.sep + 'flask'):
        run_migrations(app)
        setup_jwt(app)
        setup_request_handling(app, api_base_url)

    server.initialize()
    return app
