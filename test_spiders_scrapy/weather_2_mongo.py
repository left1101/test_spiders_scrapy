
from pymongo import MongoClient

class weather_2_mongo(object):
    def process_item(self, item, spider):
        # 将item里的数据拿出来
        date = item['date']
        temperature = item['temperature']
        wind = item['wind']
        img = item['img']

        my_client = MongoClient("mongodb://localhost:27017/")

        test_db = my_client["test"]
        customers = test_db["customers"]

        my_dict = {
            "date": date,
            "temperature": temperature,
            "wind": wind,
            "img": img,
        }

        customers.insert_one(my_dict)

        return item

