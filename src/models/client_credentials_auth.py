#!/usr/bin/env python3


class ClientCredentialsAuth:
    client_id = ""
    client_secret = ""

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def __str__(self):
        return "{ client_id: " + self.client_id + ", client_secret: " + self.client_secret + " } "
