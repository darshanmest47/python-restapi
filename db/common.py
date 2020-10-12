import configparser
import pymysql

from db import queries


class Common:
    list_datas = []
    list_dict = {}
    list_dicts_list = []
    list_dicts_keys = ['name', 'type', 'price', 'shipping', 'upc', 'description', 'manufacturer', 'model', 'url',
                       'image']

    def config_user(self):
        config = configparser.ConfigParser()
        config.read("E:\\python-restapi\\db\\connectors.ini")

        return config

    def query_exc(self, query):
        conn = pymysql.connect(host='localhost', database='users', user='root', password='tiger')

        cursor = conn.cursor()
        cursor.execute(query)

        datas = cursor.fetchall()

        for i in range(len(datas)):
            self.list_datas.append(datas[i])

        return Common.list_datas

    def gen_sql_exec(self, query):
        conn = pymysql.connect(host='localhost', database='users', user='root', password='tiger')
        cursor = conn.cursor()

        cursor.execute(query)
        conn.commit()
        cursor.close()
        # print(Common.list_datas)

    def generate_json_vals(self, datas):
        # print(datas)

        for i in range(len(datas)):
            # print(i)
            # print(Common.list_datas[i])
            # print(len(datas[i]))

            for j in range(1, len(datas[i])):
                # print(i, j)
                # print(datas[i][j])

                Common.list_dict[Common.list_dicts_keys[j - 1]] = datas[i][j]
                # print(Common.list_dicts_keys[j - 1])

            # print(Common.list_dict)
            Common.list_dicts_list.append(Common.list_dict)
            # print(Common.list_dicts_list)

            Common.list_dict = {}
            # print(Common.list_dicts_list)
            # print(Common.list_dict)

            # print()
        return Common.list_dicts_list


