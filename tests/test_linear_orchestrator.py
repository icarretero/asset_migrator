import pytest
from asset_migrator.src.base import (
    Scheduler,
    Migrator,
    Updater,
    SchedulerException,
    MigratorException,
    UpdaterException,
    OrchestratorException,
)
from asset_migrator.src.linear_orchestrator import LinearOrchestrator

class StubScheduler(Scheduler):
    def generate_jobs(self):
        pass

    def schedule(self):
        for job in ["job"]:
            yield job

class StubFailJobsScheduler(Scheduler):
    def generate_jobs(self):
        raise SchedulerException

    def schedule(self):
        pass


class StubMigrator(Migrator):
    def migrate(self, job):
        pass


class StubUpdater(Updater):
    def update(self, job):
        pass


@pytest.fixture
def green_path_components():
    return {
        'scheduler': StubScheduler(),
        'migrator': StubMigrator(),
        'updater': StubUpdater(),
    }

@pytest.fixture
def fail_jobs_generation_components():
    return {
        'scheduler': StubFailJobsScheduler(),
        'migrator': StubMigrator(),
        'updater': StubUpdater(),
    }


def test_orchestrator_requires_arguments():
    with pytest.raises(TypeError):
        LinearOrchestrator()


def test_orchestrator_can_be_initialized(green_path_components):
    LinearOrchestrator(**green_path_components)


def test_start_method_is_implemented(green_path_components):
    LinearOrchestrator(**green_path_components).start()


def test_start_method_exception_with_job_generation_failure(fail_jobs_generation_components):
    with pytest.raises(OrchestratorException):
        LinearOrchestrator(**fail_jobs_generation_components).start()
