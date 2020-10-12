import requests

from restapitest.Routes import Routes

resps = requests.get(Routes.url2, headers={'Content-Type': 'application/json'},verify=False, allow_redirects=False,timeout=2)

print(resps.history)

print(resps.status_code)
