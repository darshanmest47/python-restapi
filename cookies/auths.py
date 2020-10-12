import requests

from restapitest.Datas import Datas
from restapitest.Routes import Routes

sessions=requests.session()
sessions.auth=('darshanmesta47@hotmail.com', 'DarshanKA47@')

resp_git = requests.get(Routes.url1, auth=('darshanmesta47@hotmail.com', 'DarshanKA47@'),headers={'Content-Type': 'application/json'})
print(resp_git.status_code)
print(resp_git.json())


resp_git1=sessions.get(Routes.url1, headers={'Content-Type': 'application/json'})
print(resp_git1.status_code)
print(resp_git1.json())
