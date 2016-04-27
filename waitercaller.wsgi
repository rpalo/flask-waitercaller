#!.venv/bin/python
import sys
sys.path.insert(0, "/var/www/flask-waitercaller")
sys.path.insert(0, "/var/www/flask-waitercaller/.venv")
from waitercaller import app as application
