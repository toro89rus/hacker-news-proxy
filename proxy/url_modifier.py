from urllib.parse import urlparse, urlunparse


def to_relative_if_internal(url: str, target_url: str) -> str:
    """Return relative url if url is absolute internal.
    Otherwise keep original"""

    if not url:
        return "/"
    parsed_target = urlparse(target_url)
    parsed_url = urlparse(url)
    if parsed_url.netloc == parsed_target.netloc:
        url = make_url_relative(parsed_url)
    return url


def make_url_relative(parsed_url):
    """Return relative url"""
    return urlunparse(
        (
            "",
            "",
            parsed_url.path or "/",
            parsed_url.params,
            parsed_url.query,
            parsed_url.fragment,
        )
    )
