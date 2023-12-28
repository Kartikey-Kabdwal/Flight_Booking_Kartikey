# manage.py
import os
import sys
from dotenv import load_dotenv

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flight_booking2.settings")
    load_dotenv()
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
