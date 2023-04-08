import urllib.parse


def parse_request_client(url: str) -> dict:

    arguments = urllib.parse.urlparse(url).fragment

    return dict(urllib.parse.parse_qsl(arguments))
