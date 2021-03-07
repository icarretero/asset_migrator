import logging
from src.base import Scheduler, SchedulerException
from src.main_db import MainDB


class ListScheduler(Scheduler):
    """
        ListScheduler is a naive implementation in a List object of a Scheduler
        This won't work in prod.
    """
    BATCH_SIZE = 10

    def __init__(self, main_db):
        super().__init__()
        self.main_db= main_db
        self.jobs = []

    def generate_jobs(self):
        logging.info("SCHEDULER: starting job generation")
        jobs = self.main_db.get_jobs()
        for (id, path) in jobs:
            self.jobs.append({
                'id': id,
                'path': path
            })
        logging.info(
            "SCHEDULER: finished job generation with {items} items".format(
                items=len(self.jobs)
            )
        )

    def schedule(self):
        for job in self.jobs:
            logging.debug("SCHEDULER: scheduling next job")
            yield job
