import os.path
import re

import pytest
import responses


def stub(method, url, fixture_path=None, status_code=200):
    body = load_fixture(fixture_path) if fixture_path else '{"key":"value"}'
    responses.add(
        method, url, body=body, status=status_code, content_type="application/json"
    )


def load_fixture(fixture_path):
    return open(os.path.join(os.path.dirname(__file__), "data", fixture_path)).read()
