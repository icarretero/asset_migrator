import pytest
from unittest import mock
from src.base import DataBase, DataBaseException
from src.main_db import TableConfig, MainDB, MainDBException


JOBS = [
    ("23", "images/avatar2323.png" ),
    ("24", "images/avatar2424.png" ),
    ("25", "images/avatar2525.png" ),
    ("27", "images/avatar2626.png" ),
]


class StubDB(DataBase):
    def batch_select(self, query, batch_size):
        for item in JOBS:
            yield item


class StubEmptyDB(DataBase):
    def batch_select(self, query, batch_size):
        for item in []:
            yield item


class StubFailingDB(DataBase):
    def batch_select(self, query, batch_size):
        raise DataBaseException("ARRRRRG")


@pytest.fixture
def db():
    return StubDB()


@pytest.fixture
def empty_db():
    return StubEmptyDB()


@pytest.fixture
def failing_db():
    return StubFailingDB()


@pytest.fixture
def wrong_table_config():
    return {
        'name': 'table'
    }

@pytest.fixture
def table_config():
    return TableConfig(
        "table",
        "id",
        "path",
        "prefix1",
        "prefix2"
    )

@pytest.fixture
def query():
    return "SELECT id, path FROM table WHERE path like 'prefix1/%'"


def test_main_db_requires_arguments():
    with pytest.raises(TypeError):
        MainDB()


def test_main_db_can_be_initialized(db, table_config):
    MainDB(db, table_config)


def test_main_db_fails_with_wrong_config_object(db, wrong_table_config):
    with pytest.raises(MainDBException):
        MainDB(db, wrong_table_config)


def test_main_db_get_jobs(db, table_config):
    main_db = MainDB(db, table_config)
    jobs = main_db.get_jobs()
    assert len([ job for job in jobs]) == 4


def test_main_db_get_empty_jobs(empty_db, table_config):
    main_db = MainDB(empty_db, table_config)
    jobs = main_db.get_jobs()
    assert len([ job for job in jobs]) == 0


def test_query_called_properly(db, table_config, query):
    mock_db = mock.Mock(spec=db)
    main_db = MainDB(mock_db, table_config)
    jobs = main_db.get_jobs()
    mock_db.batch_select.assert_called_once_with(query, main_db.BATCH_SIZE)

def test_main_db_handles_database_error(failing_db, table_config):
    main_db = MainDB(failing_db, table_config)
    with pytest.raises(MainDBException):
        jobs = main_db.get_jobs()
