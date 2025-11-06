import re

from bs4 import BeautifulSoup

from proxy.url_modifier import to_relative_if_internal

TAGS_ATTRS_MAPPING = {
    "a": "href",
    "img": "src",
    "script": "src",
    "link": "href",
    "iframe": "src",
    "source": "src",
    "embed": "src",
    "form": "action",
}


def modify_html(html: str, target_url: str, symbol: str, word_len: int) -> str:
    """Modify HTML replacing all internal target url link to relative,
    add SYMBOL to all words with length of WORD_LENGTH in HTML text
    """

    soup = BeautifulSoup(html, "lxml")
    modify_links(soup, target_url)
    modify_strings(soup, symbol, word_len)
    return str(soup)


def modify_links(soup, target_url):
    """Modify all absolute internal links to relative"""
    for tag_name in TAGS_ATTRS_MAPPING:
        for tag in soup.find_all(tag_name):
            link_attr = TAGS_ATTRS_MAPPING[tag_name]
            link = tag.get(link_attr)
            if not link:
                continue
            tag[link_attr] = to_relative_if_internal(link, target_url)


def modify_strings(soup, symbol, word_len):
    """Modify all text in BS4 object"""
    for text_block in soup.find_all(string=True):
        modified_text_block = modify_string(text_block, symbol, word_len)
        text_block.replace_with(modified_text_block)


def modify_string(string: str, symbol: str, word_len: int) -> str:
    """Add symbol to all of the words of a given length in a string"""
    return re.sub(
        rf"(^|(?<=[^\w\/’]))(\w{{{word_len}}})((?=[^\w\/’])|$)",
        rf"\1\2{symbol}\3",
        string,
    )


def prettify_html(html: str | bytes):
    """Format html to a Unicode string"""
    if isinstance(html, bytes):
        html = html.decode()
    return BeautifulSoup(html, "html.parser").prettify()
