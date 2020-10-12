import requests

from restapitest.Routes import Routes

session = requests.session()
session.cookies.update({'comp': 'compulsory'})

resps = session.get(Routes.url, headers={"Content-Type": "application/json"}, cookies={'data': 'Hello'})
print(resps.text)


