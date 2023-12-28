# wsgi.py
import os
from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flight_booking2.settings")
load_dotenv()
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
