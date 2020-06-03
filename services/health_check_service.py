#!/usr/bin/env python3

import time
import schedule
from datetime import datetime
from .webapp_service import WebappService


class HealthCheckService:

    def __init__(self):
        self.schedule()

    def schedule(self):
        for webapp in WebappService().load_configuration():
            schedule.every(webapp.verification_interval_minutes).minutes.do(self.do_health_check, webapp)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def do_health_check(self, webapp):
        print(datetime.today().strftime('%Y-%m-%d %H:%M:%S') +
              ": Doing the health check of the " + webapp.name +
              " application...")
