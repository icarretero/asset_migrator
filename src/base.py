class OrchestratorException(Exception):
    pass


class SchedulerException(Exception):
    pass


class MigratorException(Exception):
    pass


class UpdaterException(Exception):
    pass


class Orchestrator:
    def __init__(self, scheduler, migrator, updater):
        self.scheduler = scheduler
        self.migrator = migrator
        self.updater = updater

    def start(self):
        raise NotImplementedError


class Scheduler:
    def generate_jobs(self):
        raise NotImplementedError

    def schedule(self):
        raise NotImplementedError


class Migrator:
    def migrate(self):
        raise NotImplementedError


class Updater:
    def update(self):
        raise NotImplementedError