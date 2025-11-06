import pytest

from proxy.headers_modifier import (
    clean_client_headers,
    clean_target_headers,
)

CLIENT_HEADERS = [
    (
        {
            "Host": "example.com",
            "User-Agent": "pytest",
            "Connection": "keep-alive",
        },
        {"User-Agent": "pytest"},
    ),
    (
        {"Accept": "text/html", "Content-Length": "123"},
        {"Accept": "text/html"},
    ),
    (
        {"X-Test": "1"},
        {"X-Test": "1"},
    ),
]

TARGET_HEADERS = [
    (
        {"Content-Encoding": "gzip", "Server": "nginx"},
        [("Server", "nginx")],
    ),
    (
        {
            "Content-Type": "text/html",
            "Referrer-Policy": "same-origin",
            "X-Frame-Options": "DENY",
        },
        [("Content-Type", "text/html")],
    ),
    (
        {"Strict-Transport-Security": "max-age=63072000", "Date": "Today"},
        [("Date", "Today")],
    ),
]


@pytest.mark.parametrize("headers, expected", CLIENT_HEADERS)
def test_clean_client_headers(headers, expected):
    assert clean_client_headers(headers) == expected


@pytest.mark.parametrize("headers, expected", TARGET_HEADERS)
def test_clean_target_headers(headers, expected):
    assert clean_target_headers(headers) == expected
