import pytest
from bs4 import BeautifulSoup

from proxy.html_modifier import (
    modify_html,
    modify_links,
    modify_string,
    modify_strings,
    prettify_html,
)
from tests.proxy.conftest import TEST_SYMBOL, TEST_URL
from tests.proxy.fixtures import (
    HTML_SIMPLE,
    HTML_SIMPLE_MODIFIED,
    HTML_WITH_LINKS_NO_TEXT,
    HTML_WITH_LINKS_NO_TEXT_MODIFIED,
    TEXT,
    TEXT_MODIFIED,
)

STRING_MODIFICATION = (
    ("", ""),
    ("word", "word"),
    ("symbol", f"symbol{TEST_SYMBOL}"),
    (TEXT, TEXT_MODIFIED),
)


HTML_STRING_MODIFICATION = (
    (HTML_SIMPLE, HTML_SIMPLE_MODIFIED),
    (HTML_WITH_LINKS_NO_TEXT, HTML_WITH_LINKS_NO_TEXT_MODIFIED),
)


HTML_LINKS_MODIFICATION = (
    ("a", "href", f"{TEST_URL}/news", "/news"),
    (
        "a",
        "href",
        "https://externalsite.com/page",
        "https://externalsite.com/page",
    ),
    (
        "img",
        "src",
        f"{TEST_URL}/static/logo.png",
        "/static/logo.png",
    ),
    ("form", "action", f"{TEST_URL}/submit", "/submit"),
)


@pytest.mark.parametrize("string, modified_string", STRING_MODIFICATION)
def test_modify_string(string, modified_string, test_symbol, test_word_len):
    assert modify_string(string, test_symbol, test_word_len) == modified_string


@pytest.mark.parametrize("html, expected_html", HTML_STRING_MODIFICATION)
def test_modify_strings(html, expected_html, test_symbol, test_word_len):
    soup = BeautifulSoup(html, "html.parser")
    modify_strings(soup, test_symbol, test_word_len)
    assert str(soup) == expected_html


@pytest.mark.parametrize("tag, attr, before, after", HTML_LINKS_MODIFICATION)
def test_modify_links_param(tag, attr, before, after, test_url):
    html = f"<{tag} {attr}='{before}'></{tag}>"
    soup = BeautifulSoup(html, "html.parser")
    modify_links(soup, test_url)
    assert soup.find(tag)[attr] == after


def test_modify_html(
    html_full, html_full_modified, test_url, test_symbol, test_word_len
):
    assert (
        prettify_html(
            modify_html(html_full, test_url, test_symbol, test_word_len)
        )
        == html_full_modified
    )
