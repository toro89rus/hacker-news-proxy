EXCLUDED_CLIENT_HEADERS = (
    "host",
    "connection",
    "content-length",
    "transfer-encoding",
)

EXCLUDED_TARGET_HEADERS = (
    "content-encoding",
    "content-length",
    "transfer-encoding",
    "connection",
    "strict-transport-security",
    "content-security-policy",
    "referrer-policy",
    "x-frame-options",
    "x-content-type-options",
    "x-xss-protection",
)


def clean_client_headers(client_headers: dict[str, str]) -> dict[str, str]:
    """Remove headers that should not be forwarded to the target site."""

    return {
        key: value
        for key, value in client_headers.items()
        if key.lower() not in EXCLUDED_CLIENT_HEADERS
    }


def clean_target_headers(
    target_headers: dict[str, str],
) -> list[tuple[str, str]]:
    """Remove headers from target site that should not be forwarded to
    client.
    Returns list of (key, value) tuples for Flask response."""

    return [
        (key, value)
        for key, value in target_headers.items()
        if key.lower() not in EXCLUDED_TARGET_HEADERS
    ]
