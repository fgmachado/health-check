#!/usr/bin/env python3

from .auth_service import AuthService
from .webapp_service import WebappService
from .logging_service import LoggingService
from .scheduler_service import SchedulerService


class HealthCheckService:

    logging_service = None

    def __init__(self):
        self.logging_service = LoggingService()

    def start(self):
        scheduler_service = SchedulerService()
        scheduler_service.schedule(WebappService().load_configuration(), self.do_health_check)
        scheduler_service.run()

    def do_health_check(self, webapp):
        self.logging_service.log("Starting the health check of the " + webapp.name + " application...")

        if webapp.auth is not None:
            auth_service = AuthService()
            access_token = auth_service.do_auth(webapp.auth)
            print(access_token)
