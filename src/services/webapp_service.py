#!/usr/bin/env python3

import yaml
from src.models.auth import Auth
from src.models.webapp import Webapp
from src.models.passowrd_auth import PasswordAuth
from src.models.client_credentials_auth import ClientCredentialsAuth


class WebappService:
    webapps = []

    def load_configuration(self):
        with open("./src/config/webapps.yml") as file:
            try:
                document = yaml.safe_load(file)
                return self.parse_apps(document.get("webapps"))
            except yaml.YAMLError as ex:
                print(ex)

    def parse_apps(self, webapps_to_parse):
        for webapp in webapps_to_parse:
            self.webapps.append(self.parse_webapp(webapp))

        return self.webapps

    def parse_webapp(self, webapp_to_parse):
        webapp = None

        for name in webapp_to_parse.keys():
            config = webapp_to_parse[name]
            auth = None
            auth_method = None

            if config["auth"]:
                auth_config = config["auth"]
                verification_interval_minutes = config["verification_interval_minutes"]
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

            webapp = Webapp(name, config["url"], verification_interval_minutes, auth)

        return webapp
