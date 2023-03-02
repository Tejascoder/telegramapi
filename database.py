
from pymongo import MongoClient

# mylib_Url=  'mongodb+srv://christorf32:welcome123%40123@cluster0.3ojjt.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE'
mylib_Url = "mongodb+srv://tejas22t:Coder123%21@mycluster.gmaql.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE"
# database
Client = MongoClient(mylib_Url, connect=False)
db = Client['telegram']
Registered_users = db['users']
users_screenshot= db['paymentscreenshot']