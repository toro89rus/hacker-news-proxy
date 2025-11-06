import pytest

import tests.proxy.fixtures as fixtures
from proxy.app import app
from proxy.html_modifier import prettify_html

TEST_URL = "https://example.com"
TEST_SYMBOL = "™"
TEST_WORD_LEN = 6


@pytest.fixture
def client():
    app.config.update(
        {
            "TARGET_URL": TEST_URL,
            "SYMBOL": TEST_SYMBOL,
            "WORD_LEN": TEST_WORD_LEN,
        }
    )
    with app.test_client() as client:
        yield client


@pytest.fixture
def html_simple():
    return prettify_html(fixtures.HTML_SIMPLE)


@pytest.fixture
def html_simple_modified():
    return prettify_html(fixtures.HTML_SIMPLE_MODIFIED)


@pytest.fixture
def html_full():
    return prettify_html(fixtures.HTML_FULL)


@pytest.fixture
def html_full_modified():
    return prettify_html(fixtures.HTML_FULL_MODIFIED)


@pytest.fixture
def test_url():
    return TEST_URL


@pytest.fixture
def test_symbol():
    return TEST_SYMBOL


@pytest.fixture
def test_word_len():
    return TEST_WORD_LEN
