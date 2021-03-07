import mariadb
from dataclasses import dataclass

class DataBaseException(Exception):
    pass

@dataclass
class DataBaseConfig:
    user: str
    password: str
    database: str
    host: str = "127.0.0.1"
    port: str = 3306

class DataBase:

    def __init__(self, dbconfig):
        self.dbconfig = dbconfig
        self.conn = self._get_connection()
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
        return conn

    def _get_cursor(self):
        return self.conn.cursor()

    def _batch_iterator(self, batch_size=1000):
        while True:
            results = self.cursor.fetchmany(batch_size)
            if not results:
                break
            for result in results:
                yield result

    def test_database(self):
        self.cursor.execute(
            "SELECT 1;"
        )

    def close(self):
        self.conn.close()

    def all_jobs(self, table, id_column, id_path, batch_size):
        query = "SELECT {id}, {path} FROM {table}".format(
            id=id_column,
            path=id_path,
            table=table
        )
        self.cursor.execute(query)
        return self._batch_iterator(batch_size)
