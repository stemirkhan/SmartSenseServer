import os

DEBUG = True

PATH_CERTIFICATE = 'certificate.pem'
PATH_PRIVATE_KEY = 'private.pem'

if DEBUG:
    PORT = 8888
    HOST = '192.168.0.100'
    ACCESS_TOKEN = 'f7f0391dc01b4261fa09d4c26cbda146081c4820ceffb0e4c453c0a41a057ceccec' \
                   '074cd2423246d206d018ed9a9396db100df5b7bc32616151217893eab1fc4'


else:
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    PORT = 53344
    HOST = '0.0.0.0'
