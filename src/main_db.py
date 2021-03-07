import mariadb
from dataclasses import dataclass

@dataclass
class TableConfig:
    name: str
    id_name: str
    path_name: str

class MainDB:

    BATCH_SIZE = 10

    def __init__(self, database, table_config):
        self.database = database
        self.table_config = table_config

    def get_jobs(self):
        query = "SELECT {id}, {path} FROM {table}".format(
            id=self.table_config.id_name,
            path=self.table_config.path_name,
            table=self.table_config.name
        )
        return self.database.batch_select(query, self.BATCH_SIZE)

    def update_jobs(self):
        pass
