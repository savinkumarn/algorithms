import requests
import json
# defining the api-endpoint
API_ENDPOINT = "https://api.random.org/json-rpc/1/invoke"

# your API key here
API_KEY = "f081c25f-36ce-43f6-9380-f89e11866cfb"

# data to be sent to api
data = r'''{
        "jsonrpc":"2.0",
        "method":"generateIntegers",
        "params":
                {"apiKey": "API_KEY",
                 "n": 10,
                 "min": 1,
                 "max": 10,
                 "replacement": false,
                 "base": 10
                 },
        "id": 21911
        }'''


def get_list_for_testing(number_of_records):
    req_data = json.loads(data)
    req_data['params']['apiKey'] = API_KEY
    req_data['params']['n'] = number_of_records
    req_data['params']['max'] = number_of_records
    resp = requests.post(url=API_ENDPOINT, json=req_data)
    print (resp.json())
    return resp.json()['result']['random']['data']
