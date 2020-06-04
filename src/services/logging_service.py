#!/usr/bin/env python3

from datetime import datetime


class LoggingService:

    def log(self, text):
        print(datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ": " + text)
