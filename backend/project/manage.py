#!/usr/bin/env python
import os
import sys
from utils.get_secret import get_secret

if __name__ == "__main__":
    module = get_secret("DJANGO_SETTINGS_MODULE", None)
    if module:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", module)
    else:
        # для случая запуска локально без докера
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.dev")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
