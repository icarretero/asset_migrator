import logging
from src.linear_orchestrator import LinearOrchestrator
from src.list_scheduler import ListScheduler
from src.copy_migrator import CopyMigrator
from src.one_updater import OneUpdater
from src.main_db import MainDB, TableConfig
from src.maria_db import MariaDB, MariaDBConfig


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

DB_CONFIG = MariaDBConfig(
    "root",
    "patata",
    "assets"
)

ASSET_TABLE_CONFIG = TableConfig(
    "assets",
    "entry_id",
    "path"
)

def main():
    main_db = MainDB(
        database=MariaDB(
            db_config=DB_CONFIG
        ),
        table_config=ASSET_TABLE_CONFIG
    )
    orchestrator = LinearOrchestrator(
        scheduler=ListScheduler(main_db),
        migrator=CopyMigrator(),
        updater=OneUpdater()
    )
    orchestrator.start()


if __name__ == "__main__":
    main()
