from urllib.parse import urlparse

import pytest

from proxy.url_modifier import (
    make_url_relative,
    to_relative_if_internal,
)
from tests.proxy.conftest import TEST_URL

relative_urls = [
    ("", "/"),
    (f"{TEST_URL}", "/"),
    (f"{TEST_URL}/", "/"),
    (f"{TEST_URL}/news", "/news"),
    (f"{TEST_URL}/news;params?p=2#section", "/news;params?p=2#section"),
    ("news", "news"),
]

absolute_url = [
    ("https://externalsite.com/news", "https://externalsite.com/news")
]


@pytest.mark.parametrize("url, internalised_url", relative_urls + absolute_url)
def test_internalize_url(url, internalised_url, test_url):
    assert to_relative_if_internal(url, test_url) == internalised_url


@pytest.mark.parametrize("url, internalised_url", relative_urls)
def test_make_url_relative(url, internalised_url):
    parsed_url = urlparse(url)
    assert make_url_relative(parsed_url) == internalised_url
