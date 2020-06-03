#!/usr/bin/env python3

from services.health_check_service import HealthCheckSevice

try:
    HealthCheckSevice().run()
except KeyboardInterrupt:
    print("Application interrupted by user...")
