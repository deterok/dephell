# project
from dephell.config import Config


def test_load():
    config = Config()
    config.attach_file(path='./tests/requirements/dephell.toml', env='some_env')
    assert config['from']['format'] == 'pip'
