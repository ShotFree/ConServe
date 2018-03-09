#!/usr/bin/python

import requests


url="http://192.168.1.222/test/get"

payload={'year': "2018"}
r = requests.get(url, params=payload)

print r.status_code
print r.content