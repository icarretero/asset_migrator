import logging
from src.base import Migrator, MigratorException


class CopyMigrator(Migrator):
    def migrate(self, job):
        logging.debug("MIGRATOR: starting job migration")
        logging.debug("MIGRATOR: finished job migration")
