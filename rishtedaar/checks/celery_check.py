from celery import Celery
from django.conf import settings
from kombu import Connection

def check_celery():
    try:
        project_name = settings.SETTINGS_MODULE.split('.')[0]
        # Initialize Celery with the broker URL
        app = Celery(project_name, broker=settings.CELERY_BROKER_URL)
        
        # Test the connection to the broker directly
        with Connection(settings.CELERY_BROKER_URL) as conn:
            conn.connect()
        
        return True, "Celery broker is reachable"
    except Exception as e:
        return False, f"Celery broker error: {str(e)}"
