import logging
from src.base import Updater, UpdaterException


class OneUpdater(Updater):
    def update(self, job):
        logging.debug("UPDATER: starting update job")
        logging.debug("UPDATER: finished update job")
