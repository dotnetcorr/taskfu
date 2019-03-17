import os
import requests

class Bot:

    def __init__(self, token):
        self.token = token
        
    def get_incoming(self):
        params = {
            'timeout': 1,
        }
        response = requests.post("https://api.telegram.org/bot%s/getMe" % self.token, params=params, timeout=10)
        if response.ok:
            print(response)
        

if __name__ == "__main__":
    bot = Bot(os.environ["TASKFU_TOKEN"])
    bot.get_incoming()