from http.server import HTTPServer
from handler import HTTPRequestHandler
from settings import *
from ssl import SSLContext, PROTOCOL_TLS_SERVER


if __name__ == '__main__':
    httpd = HTTPServer((HOST, PORT), HTTPRequestHandler)
    sslctx = SSLContext(PROTOCOL_TLS_SERVER)
    sslctx.load_cert_chain(certfile=PATH_CERTIFICATE, keyfile=PATH_PRIVATE_KEY)
    httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()

