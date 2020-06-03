#!/usr/bin/env python3

from services.health_check_service import HealthCheckService

try:
    HealthCheckService().run()
except KeyboardInterrupt:
    print("Application interrupted by user...")
