#!/usr/bin/env python3

import requests
from .logging_service import LoggingService
from ..models.passowrd_auth import PasswordAuth
from ..models.client_credentials_auth import ClientCredentialsAuth


class AuthService:

    logging_service = None

    def __init__(self):
        self.logging_service = LoggingService()

    def do_auth(self, auth):
        if auth.method == "POST":
            try:
                response = requests.post(auth.url, self.get_auth_body(auth))
                print(response)
            except (ConnectionError, ConnectionRefusedError, WindowsError):
                self.logging_service.log("Unable to open connection with " + auth.url)

        return "my_fake_token"

    def get_auth_body(self, auth):
        data = None

        if auth.grant_type == "password" and type(auth) is PasswordAuth:
            auth = PasswordAuth(auth)
            data = '''
                {
                    "grant_type": ''' + auth.grant_type + ''',
                    "username": ''' + auth.username + ''',
                    "password": ''' + auth.password + '''
                }
            '''
        elif auth.grant_type == "client_credentials":
            auth = ClientCredentialsAuth(auth)
            data = '''
                {
                    "grant_type": ''' + auth.grant_type + ''',
                    "client_id": ''' + auth.client_id + ''',
                    "client_secret": ''' + auth.client_secret + '''
                }
            '''

        return data
