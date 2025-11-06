import pook

from proxy.html_modifier import prettify_html


@pook.on
def test_proxy_simple_html(
    client, test_url, html_simple, html_simple_modified
):
    pook.get(
        test_url,
        reply=200,
        response_type="text/html",
        response_body=html_simple,
    )
    response = client.get("/")
    assert response.status_code == 200
    assert prettify_html(response.data) == html_simple_modified


@pook.on
def test_proxy_full_html(client, test_url, html_full, html_full_modified):
    pook.get(
        test_url,
        reply=200,
        response_type="text/html",
        response_body=html_full,
    )
    response = client.get("/")

    assert response.status_code == 200
    assert prettify_html(response.data) == html_full_modified


@pook.on
def test_proxy_redirect(client, test_url):
    pook.get(
        test_url,
        reply=302,
        response_headers={"Location": "https://example.com/news"},
    )
    response = client.get("/")

    assert response.status_code == 302
    assert response.headers["Location"] == "/news"


@pook.on
def test_proxy_not_html(client, test_url):
    body = b"binary-image-data"
    pook.get(
        test_url,
        reply=200,
        response_type="image/png",
        response_body=body,
    )
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"
    assert response.data == body
