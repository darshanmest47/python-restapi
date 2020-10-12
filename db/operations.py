import requests

from db import queries
from db.common import Common
from db.routes import Routes

config = Common().config_user()
common = Common()


class Operations:
    ids = []

    def getop(self):
        res = requests.get(config['API']['apis'] + Routes.endpoints, headers={"Content-Type": "application/json"})

        print(res.status_code)
        print(res.json())

    def postop(self):
        pass

    def queryexec(self, query):
        return common.query_exc(query)

    def gen_sql(self, query):
        common.gen_sql_exec(query)

    def generate_Json(self, query_data):
        return common.generate_json_vals(query_data)

    def indi_json(self, datas):
        print(len(datas))
        # common.generate_individual_json(datas)
        for i in range(len(datas)):
            # print(datas[i])
            # return datas[i]
            post_res = requests.post(config['API']['apis'] + Routes.endpoints, json=datas[i],
                                     headers={"Content-Type": "application/json"})
            print(post_res.json())
            print(post_res.json()['id'])
            Operations.ids.append(post_res.json()['id'])

        # print(Operations.ids)

        return Operations.ids

    def get_pros_by_id(self, ids):
        print()
        for j in range(len(ids)):
            print(f'Getting the details by id {ids[j]}......')

            fetch_on_edit = requests.get(config['API']['apis'] + Routes.endpoints + str(ids[j]),
                                         headers={"Content-Type": "application/json"})
            print(fetch_on_edit.json())
            print('Fetching by id complete')
            print()

        for k in range(len(ids)):
            print(ids[k])
            self.edit_by_id(ids[k])
            break
            # self.edit_by_id(ids[k+1])

    def edit_by_id(self, id):
        print(f'edit by id {id} is in progeress....')

        edit_conf = requests.patch(config['API']['apis'] + Routes.endpoints + str(id), json=queries.data_to_patch,
                                   headers={"Content-Type": "application/json"})
        print(edit_conf.json())
        print(edit_conf.status_code)

        print(f'edit by id {id} completed...')

        self.delete_by_id(id)

    def delete_by_id(self, id):
        print(f'Delete by id {id} is in progress')

        del_resp = requests.delete(config['API']['apis'] + Routes.endpoints + str(id))

        print(del_resp.status_code)
        print(f'deletion by id {id} success')
