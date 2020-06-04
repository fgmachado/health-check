#!/usr/bin/env python3

from src.services.health_check_service import HealthCheckService

try:
    HealthCheckService().start()
except KeyboardInterrupt:
    print("Application interrupted by user...")
