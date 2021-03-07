import pytest
from src.list_scheduler import ListScheduler


JOBS = [
    ("23", "images/avatar2323.png" ),
    ("24", "images/avatar2424.png" ),
    ("25", "images/avatar2525.png" ),
    ("27", "images/avatar2626.png" ),
]


class StubMainDB():
    def get_jobs(self):
        for item in JOBS:
            yield item


class StubEmptyMainDB():
    def get_jobs(self):
        for item in []:
            yield item


@pytest.fixture
def main_db():
    return StubMainDB()


@pytest.fixture
def empty_main_db():
    return StubEmptyMainDB()


def test_scheduler_requires_arguments():
    with pytest.raises(TypeError):
        ListScheduler()


def test_scheduler_can_be_initialized(main_db):
    ListScheduler(main_db)


def test_scheduler_schedules_jobs(main_db):
    scheduler = ListScheduler(main_db)
    scheduler.generate_jobs()
    assert len(scheduler.jobs) == 4


def test_scheduler_schedules_empty_jobs(empty_main_db):
    scheduler = ListScheduler(empty_main_db)
    scheduler.generate_jobs()
    assert len(scheduler.jobs) == 0
