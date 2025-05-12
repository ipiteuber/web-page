import os
import oracledb

oracledb.init_oracle_client(lib_dir="/home/meow/oracle/instantclient_23_8")
os.environ["TNS_ADMIN"] = "/home/meow/oracle_wallet" 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_page.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
