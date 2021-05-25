# Create your tasks here

from celery import shared_task
from .models import Rutina, Note
from .allntbk import RutinaNotebooks

from .solotodo import get_api_info
import requests
from bs4 import BeautifulSoup
import re
import json



@shared_task
def get_ntbk_data():
    RutinaNotebooks()
