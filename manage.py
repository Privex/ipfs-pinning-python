#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv
from pathlib import Path


def main():
    """Run administrative tasks."""
    # Deal with the issue of conflicting dotenv packages by trying both methods...
    base_dir = Path(__file__).resolve().parent
    env_file = str(base_dir / '.env')
    try:
        dotenv.load_dotenv(env_file)
    except AttributeError:
        dotenv.read_dotenv(env_file)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pincore.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
