import logging
from src.base import Updater, UpdaterException


class OneUpdater(Updater):
    def update(self, job):
        logging.debug("UPDATER: starting job update")
        logging.debug("UPDATER: finished job update")
