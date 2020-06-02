#!/usr/bin/env python3

import yaml


class Webapp:
    name = ""
    url = ""
    auth = None

    def __init__(self, name, url, auth=None):
        self.name = name
        self.url = url
        self.auth = auth

    def __str__(self):
        return "{ name: " + str(self.name) + ", url: " + str(self.url) + ", auth: " + self.auth.__str__() + " }"


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


class ClientCredentialsAuth:
    client_id = ""
    client_secret = ""

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def __str__(self):
        return "{ client_id: " + self.client_id + ", client_secret: " + self.client_secret + " } "


class PasswordAuth:
    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return "{ username: " + self.username + ", password: " + self.password + " } "


class WebappService:
    webapps: []

    def load_configuration(self):
        with open("./config/webapps.yml") as file:
            try:
                document = yaml.safe_load(file)
                self.parse_apps(document.get("webapps"))
            except yaml.YAMLError as ex:
                print(ex)

    def parse_apps(self, webapps_to_parse):
        for webapp in webapps_to_parse:
            self.parse_webapp(webapp)

    def parse_webapp(self, webapp_to_parse):
        for name in webapp_to_parse.keys():
            config = webapp_to_parse[name]
            auth = None
            auth_method = None

            if config["auth"]:
                auth_config = config["auth"]
                auth_method = None
                grant_type = auth_config.get("grant_type")

                if grant_type == "password":
                    auth_method = PasswordAuth(auth_config["username"], auth_config["password"])
                elif grant_type == "client_credentials":
                    auth_method = ClientCredentialsAuth(auth_config["client_id"], auth_config["client_secret"])

                auth = Auth(auth_config["url"],
                            auth_config["method"],
                            auth_config["grant_type"],
                            auth_method,
                            auth_config["headers"])

            webapp = Webapp(name, config["url"], auth)
            print(webapp)


webapp_service = WebappService()
webapp_service.load_configuration()
