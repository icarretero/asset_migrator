from asset_migrator.src.base import Orchestrator, OrchestratorException

"""
    LinearOrchestrator is a sequencial orchestrator without concurrency:
    - It requests the scheduler for one job.
    - The job is sent to the migrator
    - Then it is sent to the updater
    - Sends the update to the scheduler
"""
class LinearOrchestrator:

    def start(self):
        pass
