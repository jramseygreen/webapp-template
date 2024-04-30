from app import create_app
from backend.server import server

# to make a migration - flask db migrate -m "message here"
# to make a migration without schema changes - flask db revision -m "message here"

server.set_host('0.0.0.0')
server.set_port(8085)
server.set_num_workers(10)

app = create_app(server)

server.start()
