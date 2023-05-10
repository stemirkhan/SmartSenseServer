import os

# SSL
PATH_CERTIFICATE = 'certificate.pem'
PATH_PRIVATE_KEY = 'private.pem'

# Server
PORT = os.getenv("SERVER_PORT")
HOST = os.getenv("SERVER_HOST")

# Log
ERROR_SERVER_LOG_FILE = './error_server.log'
ERROR_DB_LOG_FILE = './error_db.log'
LOG_SIZE = 5  # Size in megabytes

# DB
SENSOR_READINGS_TABLE = 'sensor_readings'
USER_DB = os.getenv("USER_DB")
HOST_DB = os.getenv("HOST_DB")
PORT_DB = os.getenv("PORT_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
DATABASE = os.getenv("DATABASE")
