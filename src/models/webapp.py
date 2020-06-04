#!/usr/bin/env python3


class Webapp:
    name = ""
    url = ""
    verification_interval_minutes = 1
    auth = None

    def __init__(self, name, url, verification_interval_minutes, auth=None):
        self.name = name
        self.url = url
        self.verification_interval_minutes = verification_interval_minutes
        self.auth = auth

    def __str__(self):
        return "{ name: " + str(self.name) + \
               ", url: " + str(self.url) + \
               ", verification_interval_minutes: " + str(self.verification_interval_minutes) + \
               ", auth: " + self.auth.__str__() + \
               " }"
