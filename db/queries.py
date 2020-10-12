query = "select * from products;"

query1 = "INSERT into products values ('1234'," \
         "'windows laptop 2021', " \
         "'standard laptop 2021'," \
         " 40000, " \
         "600," \
         " 'simple 2021'," \
         " 'windows 2021 edition'," \
         " 'Microsoft'," \
         " 'windows 10 2021'," \
         " 'https://www.windows20201.com'," \
         " 'img2021.png');"

query2 = "UPDATE products set id=3 WHERE id=12345"

data_to_patch = {
    "name": "windows laptop 2100",
    "type": "windows laptop",
    "price": 40000,
    "shipping": 1000,
    "upc": "2100 edition",
    "description": "windows 2100 edition laptop",
    "manufacturer": "Microsoft",
    "model": "windows 2100",
    "url": "https://www.windows2100.com",
    "image": "img2100.jpg"
}
