import requests
import os

name ='warenix'
screen_name = 'warenix'
text = 'hi'
gcm_api_key = os.environ['GCM_API_KEY']
gcm_url = 'http://exp-warenix.rhcloud.com/gcm/sendMessage1to1'

data  = {
        'name': name,
        'screen_name': screen_name,
        'text': text
}
payload = {
        'data': data,
        'api_key': gcm_api_key,
        'reg_id_list':[os.environ['REG_ID']]
}
r = requests.post(gcm_url, json=payload)
print r.text


