#!/usr/bin/env python3


class PasswordAuth:
    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return "{ username: " + self.username + ", password: " + self.password + " } "
