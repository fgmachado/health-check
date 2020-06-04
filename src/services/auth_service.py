#!/usr/bin/env python3

import json
import requests
from .logging_service import LoggingService


class AuthService:

    logging_service = None

    def __init__(self):
        self.logging_service = LoggingService()

    def do_auth(self, auth):
        token = None

        if auth.method == "POST":
            try:
                response = requests.post(auth.url, data=self.get_auth_body(auth), headers=auth.headers)
                content = json.loads(response.text)
                token = content["access_token"]
            except (ConnectionError, ConnectionRefusedError, WindowsError):
                self.logging_service.log("Unable to open connection with " + auth.url)

        return token

    def get_auth_body(self, auth):
        data = None

        if auth.grant_type == "password":
            data = {
                "grant_type": auth.grant_type,
                "username": auth.authorization.username,
                "password": auth.authorization.password
            }
        elif auth.grant_type == "client_credentials":
            data = {
                "grant_type": auth.grant_type,
                "client_id": auth.authorization.client_id,
                "client_secret": auth.authorization.client_secret
            }

        return data
