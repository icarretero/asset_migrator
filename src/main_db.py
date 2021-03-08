from dataclasses import dataclass
from src.base import DataBase, DataBaseException

class MainDBException(Exception):
    pass

@dataclass
class TableConfig:
    name: str
    id_name: str
    path_name: str
    old_prefix: str
    new_prefix: str

class MainDB:

    BATCH_SIZE = 10

    def __init__(self, database, table_config):
        if isinstance(database, DataBase):
            self.database = database
        else:
            raise MainDBException("Wrong DataBase objet. Must be a DataBase")
        if isinstance(table_config, TableConfig):
            self.table_config = table_config
        else:
            raise MainDBException("Wrong TableConfig objet. Must be a TableConfig")

    def get_jobs(self):
        query = "SELECT {id}, {path} FROM {table} WHERE {path} like '{prefix}/%'".format(
            id=self.table_config.id_name,
            path=self.table_config.path_name,
            table=self.table_config.name,
            prefix=self.table_config.old_prefix
        )
        try:
            jobs = self.database.batch_select(query, self.BATCH_SIZE)
        except DataBaseException as e:
            raise MainDBException("DataBase Error") from e
        return jobs

    def update_jobs(self):
        pass
