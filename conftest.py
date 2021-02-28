import os
import time
import pytest
import logging


def read_file(path):
    with open(os.path.join(os.path.dirname(__file__), path)) as input_file:
        return input_file.read()


@pytest.fixture(scope="session")
def jwt_auth_header():
    jmt_token = read_file("data/jwt_token.txt")
    return dict(Authorization="Bearer " + jmt_token)


def pytest_configure(config):
    timestamp = time.strftime('%Y%m%d%H%M%S')
    config.option.htmlpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results\\vonage_reports_' + timestamp + '.html')

    logging.basicConfig(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), "results\\vonage_" + timestamp + ".log"),
                        level=logging.DEBUG,
                        format='%(asctime)s %(name)s::%(funcName)s() [%(levelname)s] - %(message)s')
