# settings.py
# importing the load_dotenv from the python-dotenv module
from tokenize import group
from dotenv import load_dotenv

# using existing module to specify location of the .env file
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# retrieving keys and adding them to the project
# from the .env file through their key names
ZabbixAPI_URL = os.getenv("ZabbixAPI_URL")
Zabbix_Login = os.getenv("Zabbix_Login")
Zabbix_Password = os.getenv("Zabbix_Password")

Services_tag=os.getenv("Services_tag")
alert_tag=os.getenv("alert_tag")
Location_tag=os.getenv("Location_tag")

group=os.getenv("group")