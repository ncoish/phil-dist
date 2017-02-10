import requests
import msgpack
import lxml
from bs4 import BeautifulSoup as BS

def investigate_page(url):
    # Get page