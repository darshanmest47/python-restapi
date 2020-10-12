import requests

from restapitest.Routes import Routes

path = "C:\\Users\\Darshan\\Desktop\\questionpapers\\DRDO\\TIER 1\\Arithmetic.pdf"

files = {'file': open(path, 'rb')}

resps=requests.post(Routes.url3, files=files)
print(resps.status_code)
print(resps.text)
