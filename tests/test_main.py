from asset_migrator.main import AssetMigrator

def test_main_says_hello():
    migrator = AssetMigrator()
    assert migrator.say_hello() == "Hello World"
