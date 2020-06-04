#!/usr/bin/env python3

import time
import schedule


class SchedulerService:

    def schedule(self, webapps, task):
        for webapp in webapps:
            schedule.every(webapp.verification_interval_minutes).minutes.do(task, webapp)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
