import logging
from src.linear_orchestrator import LinearOrchestrator
from src.list_scheduler import ListScheduler
from src.copy_migrator import CopyMigrator
from src.one_updater import OneUpdater
from src.database import DataBaseConfig


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


def main():
    dbconfig = DataBaseConfig(
        "root",
        "patata",
        "assets"
    )
    orchestrator = LinearOrchestrator(
        scheduler=ListScheduler(dbconfig),
        migrator=CopyMigrator(),
        updater=OneUpdater()
    )
    orchestrator.start()


if __name__ == "__main__":
    main()
