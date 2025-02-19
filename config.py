#All the configuration parameters are defined here
#This file is imported in all the other files where the configuration parameters are required

rmqhost = '192.168.4.226'
rmqport = 5672
rmqvhost = '/dan_vhost'
rmqusername = 'dan_user'
rmqpassword = '123'
routing_key_name = 'dan_routing_key'
#note: string dari mqttbox ke mqtt ==> { "value": 123 } perhatikan petiknya, sedangkan json yang dikirim ke mongodb ==> { 'value': 123 }

mongodburi = 'mongodb://localhost:27017/'
db_name = 'testdb'
collection_name = 'satu'