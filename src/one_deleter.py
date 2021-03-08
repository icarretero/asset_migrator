import logging
from src.base import Deleter, DeleterException


class OneDeleter(Deleter):
    def delete(self, job):
        logging.debug("DELETER: starting deletion job")
        logging.debug("DELETER: finished deletion job")
