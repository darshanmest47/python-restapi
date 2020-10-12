import configparser


class Datas:

    def config_pars(self):
        config = configparser.ConfigParser()
        config.read("E:\\python-restapi\\restapitest\\params.ini")

        return config

    def json_data(self):
        data = {
            "name": "Windows-10 Lappy",
            "type": "Laptop",
            "price": 12000,
            "shipping": 200,
            "upc": "upsp",
            "description": "a simple standard lappy",
            "manufacturer": "abcd",
            "model": "2020",
            "url": " https://www.windows10.com",
            "image": "windows10.png"
        }

        return data

    def patch_json_data(self):
        datas = {
            "name": "Windows-10 Laptop",
            "type": "Laptop-windows10",
            "price": 15000,
            "shipping": 500,
            "upc": "upsp",
            "description": "a simple standard laptop",
            "manufacturer": "abcdefgh",
            "model": "2020",
            "url": " https://www.windows10.com",
            "image": "windows10-2020.png"
        }
        return datas
