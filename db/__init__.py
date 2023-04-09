from psycopg2 import connect


class WorkerDB:
    def __init__(self, user: str, password: str, host: str, port: str, database: str):
        self.connection_db = connect(user=user,
                                     password=password,
                                     host=host,
                                     port=port,
                                     database=database)
        self.cursor = self.connection_db.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS sensor_readings("
                            "id serial NOT NULL primary key,"
                            "recording_time TIMESTAMP NOT NULL DEFAULT now(),"
                            "temperature double precision,"
                            "pressure double precision,"
                            "carbon_monoxide double precision,"
                            "humidity double precision);")
        self.connection_db.commit()

    def add_measurements(self, temperature: str,
                         pressure: str,
                         carbon_monoxide: str,
                         humidity: str):
        sql_command = """
                    INSERT INTO sensor_readings (
                    temperature, 
                    pressure,
                    carbon_monoxide,
                    humidity) 
                    VALUES (%s, %s, %s, %s);"""

        self.cursor.execute(sql_command, (float(temperature), float(pressure), float(carbon_monoxide), float(humidity)))
        self.connection_db.commit()

    def __del__(self):
        self.connection_db.close()
