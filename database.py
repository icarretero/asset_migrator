import mariadb
from dataclasses import dataclass

class DataBaseException(Exception):
    pass

@dataclass
class DataBaseConfig:
    user: str
    password: str
    database: str
    host: str = "localhost"
    port: str = 3306

class DataBase:
    def __init__(self, dbconfig):
        self.dbconfig = dbconfig
        self.cursor = self._get_cursor()

    def _get_connection(self):
        try:
            conn = mariadb.connect(
                user=self.dbconfig.user,
                password=self.dbconfig.password,
                database=self.dbconfig.database,
                host=self.dbconfig.host,
                port=self.dbconfig.port,
            )
        except mariadb.Error as e:
            raise DataBaseException(e)

    def _get_cursor(self):
        conn = self._get_connection()
        return conn.cursor()

    def test_database(self):
        self.cursor.execute(
            "SELECT 1;"
        )
