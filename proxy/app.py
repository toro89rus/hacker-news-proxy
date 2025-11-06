import requests
from flask import Flask, current_app, make_response, request
from requests.exceptions import ConnectionError, HTTPError, Timeout

from proxy import messages
from proxy.headers_modifier import (
    clean_client_headers,
    clean_target_headers,
)
from proxy.html_modifier import modify_html
from proxy.settings import SYMBOL, TARGET_URL, WORD_LEN
from proxy.url_modifier import to_relative_if_internal

app = Flask(__name__, static_folder=None)
app.config["TARGET_URL"] = TARGET_URL
app.config["SYMBOL"] = SYMBOL
app.config["WORD_LEN"] = WORD_LEN

METHODS = ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]


@app.route("/", methods=METHODS)
@app.route("/<path:subpath>", methods=METHODS)
def handle_request(subpath=""):
    try:
        query_params = request.args.to_dict()
        forwarded_headers = clean_client_headers(request.headers)
        target_url = current_app.config["TARGET_URL"]
        full_path = f"{target_url}/{subpath}"
        data = request.form.to_dict()
        target_response = requests.request(
            method=request.method,
            url=full_path,
            params=query_params,
            data=data,
            cookies=request.cookies,
            headers=forwarded_headers,
            allow_redirects=False,
        )
        if 300 <= target_response.status_code < 400:
            location_url = target_response.headers.get("Location")
            target_response.headers["Location"] = to_relative_if_internal(
                location_url, target_url
            )
        modified_hn_headers = clean_target_headers(target_response.headers)
        if "text/html" in target_response.headers.get("Content-Type", ""):
            symbol = current_app.config["SYMBOL"]
            word_len = current_app.config["WORD_LEN"]
            content_to_return = modify_html(
                target_response.text, target_url, symbol, word_len
            )
        else:
            content_to_return = target_response.content
        proxy_response = make_response(
            content_to_return, target_response.status_code, modified_hn_headers
        )

    except (HTTPError, Timeout, ConnectionError) as exc:
        return f"{messages.CONNECTION_ERROR} - {str(exc)}"
    return proxy_response
