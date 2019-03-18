import os
import requests
import socks
import time

PROXY_LIST = {"https":"socks5://127.0.0.1:9150"}

class Bot:

    def __init__(self, token):
        self.token = token
        self.incoming = []
        
    def get_incoming(self):
        params = {
            'timeout': 1,
        }
        r = requests.post("https://api.telegram.org/bot%s/getUpdates" % self.token, params=params, timeout=10, proxies=PROXY_LIST)
        if r.ok:
            response = r.json()
            print(response)

            if response['result']:
                for item in response['result']:
                    self.update_id = item['update_id']
                    if 'message' in item:
                        self.incoming.append(item['message'])
                    elif 'edited_message' in item:
                        self.incoming.append(item['edited_message'])
                
    
    def start(self, timeout=2):
        while True:
            self.get_incoming()

            if self.incoming:
                for message in self.incoming:
                    chat_id = message['chat']['id']
                    message_id = message['message_id']
            else:
                time.sleep(timeout)
            


if __name__ == "__main__":
    bot = Bot(os.environ["TASKFU_TOKEN"])
    bot.start()