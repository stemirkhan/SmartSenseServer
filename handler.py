from http.server import BaseHTTPRequestHandler
from utils import parse_request_client
from settings import ACCESS_TOKEN
from db import WorkerDB

db = WorkerDB('postgres', 'qwe', 'localhost', '5432', 'sensor_data')


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        arguments = parse_request_client(self.path)

        if arguments['access_token'] == ACCESS_TOKEN:
            db.add_measurements(arguments['temperature'],
                                arguments['pressure'],
                                arguments['carbonMonoxide'],
                                arguments['humidity'])
            self.send_response(200)

        else:
            self.send_response(401)

        self.end_headers()
        self.wfile.write(b'')
