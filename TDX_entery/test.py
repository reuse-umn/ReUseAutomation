#!/usr/bin/env python3
import requests
import json
url = 'https://tdx.umn.edu/TDWebApi/api/auth/login'
header = {'Content-Type':'applicaton/json'}
body = {'UserName':'imdie022@umn.edu', 'Password':'AppleMangoPie1234'}

response = requests.post(url, data=json.dumps(body), headers=header)

print(response)
