from TwitterAPI import *
import requests
import os

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_SECRET']
access_token_key = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

gcm_api_key = os.environ['GCM_API_KEY']
gcm_url = 'http://exp-warenix.rhcloud.com/gcm/sendMessage1to1'

while True:
    try:
        #r = api.request('statuses/filter', {'track': 'hong kong', 'location': '22.25,114.1667'})
        r = api.request('user')
        iterator = r.get_iterator()
        for item in iterator:
            if 'text' in item:
                text = item['text'].encode('utf-8', 'ignore')
                name = item['user']['name'].encode('utf-8', 'ignore')
                screen_name = item['user']['screen_name'].encode('utf-8', 'ignore')
                id_str = item['id_str']
                profile_image_url = item['user']['profile_image_url']

                print  "%s(@%s)\t\t: %s" % (name, screen_name, text)
                print
                data  = {
                        'name': name,
                        'screen_name': screen_name,
                        'text': text,
                        'profile_image_url': profile_image_url,
                        'id_str': id_str
                        }
                payload = {
                        'data': data,
                        'api_key': gcm_api_key,
                        'reg_id_list':[os.environ['REG_ID']]
                        }
                r = requests.post(gcm_url, json=payload)
                print r.text
            elif 'disconnect' in item:
                event = item['disconnect']
                if event['code'] in [2,5,6,7]:
                    # something needs to be fixed before re-connecting
                    raise Exception(event['reason'])
                else:
                    # temporary interruption, re-try request
                    break
    except TwitterRequestError as e:
        if e.status_code < 500:
            # something needs to be fixed before re-connecting
            raise
        else:
            # temporary interruption, re-try request
            pass
    except TwitterConnectionError:
        # temporary interruption, re-try request
        pass

