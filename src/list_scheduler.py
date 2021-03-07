import logging
from src.base import Scheduler, SchedulerException
from src.database import DataBase


class ListScheduler(Scheduler):
    """
        ListScheduler is a naive implementation in a List object of a Scheduler
        This won't work in prod.
    """
    BATCH_SIZE = 10

    def __init__(self, dbconfig):
        super().__init__()
        self.dbconfig = dbconfig
        self.jobs = []

    def generate_jobs(self):
        logging.info("SCHEDULER: starting job generation")
        id_column = "entry_id"
        id_path = "path"
        main_db = DataBase(self.dbconfig)
        jobs = main_db.all_jobs(
            table="assets",
            id_column=id_column,
            id_path=id_path,
            batch_size=self.BATCH_SIZE
        )
        for (id, path) in jobs:
            self.jobs.append({
                'id': id,
                'path': path
            })
        main_db.close()

    def schedule(self):
        for job in self.jobs:
            logging.info("SCHEDULER: scheduling next job")
            yield job
