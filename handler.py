from http.server import BaseHTTPRequestHandler
from utils import parse_request_client, validator_url_arguments
from settings import *
from db import WorkerDB

db = WorkerDB(USER_DB, PASSWORD_DB, HOST_DB, PORT_DB, DATABASE)


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        arguments = parse_request_client(self.path)
        if validator_url_arguments(arguments) and arguments['access_token'] == ACCESS_TOKEN:
            db.add_measurements(arguments['temperature'], arguments['pressure'],
                                arguments['carbonMonoxide'], arguments['humidity'])
            self.send_response(200)

        else:
            self.send_error(401)

        self.end_headers()
        self.wfile.write(b'')
