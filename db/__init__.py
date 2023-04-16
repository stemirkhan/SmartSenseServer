from psycopg2 import connect
from log import db_logger


class WorkerDB:
    def __init__(self, user: str, password: str, host: str, port: str, database: str):
        try:
            self.connection_db = connect(user=user,
                                         password=password,
                                         host=host,
                                         port=port,
                                         database=database)

            self._cursor = self.connection_db.cursor()
        except Exception:
            db_logger.exception("Error connecting to database")

    def create_table(self):
        sql_create_table_command = """CREATE TABLE IF NOT EXISTS sensor_readings(
                                      id serial NOT NULL primary key,
                                      recording_time TIMESTAMP NOT NULL DEFAULT now(),
                                      temperature double precision,
                                      pressure double precision,
                                      carbon_monoxide double precision,
                                      humidity double precision);"""

        try:
            self._cursor.execute(sql_create_table_command)
            self.connection_db.commit()
        except Exception:
            db_logger.exception("Error creating table")

    def add_measurements(self, temperature: str,
                         pressure: str,
                         carbon_monoxide: str,
                         humidity: str):
        sql_insert_command = """
                            INSERT INTO sensor_readings (
                            temperature, 
                            pressure,
                            carbon_monoxide,
                            humidity) 
                            VALUES (%s, %s, %s, %s);"""

        try:
            self._cursor.execute(sql_insert_command,
                                (float(temperature), float(pressure), float(carbon_monoxide), float(humidity)))
            self.connection_db.commit()
        except Exception:
            db_logger.exception(f"Error adding record: {temperature}, {pressure}, {carbon_monoxide}, {humidity}")

    def __del__(self):
        self.connection_db.close()
