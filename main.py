from database import DataBase, DataBaseConfig, DataBaseException
class AssetMigrator:

    def say_hello(self):
        return "Hello World"

    def test_database(self):
        config = DataBaseConfig(
            "root",
            "password",
            "patata",
        )
        db = DataBase(config)


if __name__ == "__main__":
    AssetMigrator().test_database()
