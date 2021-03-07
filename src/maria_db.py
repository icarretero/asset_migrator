import mariadb
from dataclasses import dataclass
from src.base import DataBaseException


@dataclass
class MariaDBConfig:
    user: str
    password: str
    database: str
    host: str = "127.0.0.1"
    port: str = 3306


class MariaDB:

    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = self._get_connection()
        self.cursor = self._get_cursor()

    def _get_connection(self):
        try:
            conn = mariadb.connect(
                user=self.db_config.user,
                password=self.db_config.password,
                database=self.db_config.database,
                host=self.db_config.host,
                port=self.db_config.port,
            )
        except mariadb.Error as e:
            raise DataBaseException(e)
        return conn

    def _get_cursor(self):
        return self.conn.cursor()

    def _batch_fetch_iterator(self, batch_size=1000):
        while True:
            results = self.cursor.fetchmany(batch_size)
            if not results:
                self.close()
                break
            for result in results:
                yield result

    def test_database(self):
        self.cursor.execute(
            "SELECT 1;"
        )

    def close(self):
        self.conn.close()

    def batch_select(self, query, batch_size):
        self.cursor.execute(query)
        return self._batch_fetch_iterator(batch_size)
