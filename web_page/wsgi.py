import os
from django.core.wsgi import get_wsgi_application
import oracledb

oracledb.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_23_8")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_page.settings')
application = get_wsgi_application()
