from asset_migrator.src.base import (
    Orchestrator,
    OrchestratorException,
    SchedulerException,
    MigratorException,
    UpdaterException
)

"""
    LinearOrchestrator is a sequencial orchestrator without concurrency:
    - It requests the scheduler for one job.
    - The job is sent to the migrator
    - Then it is sent to the updater
    - Sends the update to the scheduler
"""
class LinearOrchestrator(Orchestrator):

    def __init__(self, scheduler, migrator, updater):
        super().__init__(
            scheduler=scheduler,
            migrator=migrator,
            updater=updater
        )

    def start(self):
        try:
            self.scheduler.generate_jobs()
        except SchedulerException as e:
            raise OrchestratorException(e)
        for job in self.scheduler.schedule():
            self.migrator.migrate(job)
            self.updater.update(job)
