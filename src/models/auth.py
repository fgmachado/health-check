#!/usr/bin/env python3


class Auth:
    url = ""
    method = ""
    grant_type = None
    authorization = None
    headers = None

    def __init__(self, url, method, grant_type=None, authorization=None, headers=None):
        self.url = url
        self.method = method
        self.grant_type = grant_type
        self.authorization = authorization
        self.headers = headers

    def __str__(self):
        return "{ url: " + self.url + \
               ", method: " + self.method + \
               ", grant_type: " + self.grant_type + \
               ", authorization: " + self.authorization.__str__() + \
               " }"
