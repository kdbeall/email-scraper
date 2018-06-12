# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys
import urllib3
import html5lib
from bs4 import BeautifulSoup

def job(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http = urllib3.PoolManager()
    req = http.request('GET', url)
    print(url)
    page = req.data
    soup = BeautifulSoup(page, 'html5lib')
    print([a.text for a in soup.select("a[href^=mailto:]")])

job(sys.argv[1])
