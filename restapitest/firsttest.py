import requests
import configparser

from restapitest.Datas import Datas
from restapitest.Routes import Routes

# get
# results = requests.get(config['API']['endpoint'] + Routes.products, headers={'Content-Type': 'application/json'})
# datas = results.json()
# categories = datas['data'][0]['categories']
#
# for cat in categories:
#     print(cat['name'])
#     if cat['name'] == "Housewares":
#         print(cat)
#         break
#
# print(len(datas['data']))
#
# for data in datas['data']:
#     # print(data['categories'])
#
#     for ele in data['categories']:
#         if ele['name'] == 'Alkaline Batteries':
#             print(ele)

# post


posts = requests.post(Datas().config_pars()['API']['endpoint'] + Routes.products, json=Datas().json_data(), headers={
    "Content-Type": "application/json"
})
print(posts.status_code)
print(posts.json())
item_id = posts.json()['id']
print(item_id)

# get products by id

product_bid = requests.get(Datas().config_pars()['API']['endpoint'] + Routes.products + str(item_id),
                           headers={'Content-Type': 'application/json'})
print(product_bid.status_code)
print(product_bid.json())

# patch
patch_pro = requests.patch(Datas().config_pars()['API']['endpoint'] + Routes.products + str(item_id),
                           json=Datas().patch_json_data(), headers={'Content-Type': 'application/json'})

print(patch_pro.status_code)
print(patch_pro.json())

# get after patch

product_bidpt = requests.get(Datas().config_pars()['API']['endpoint'] + Routes.products + str(item_id),
                             headers={'Content-Type': 'application/json'})
print(product_bidpt.status_code)
print(product_bidpt.json())
# delete

dels = requests.delete(Datas().config_pars()['API']['endpoint'] + Routes.products + str(item_id),
                       headers={"Content-Type": "application/json"})

print(dels.status_code)
print(dels.json())
