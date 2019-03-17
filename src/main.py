import os
import requests
import socks

# s = socks.socksocket()
# s.set_proxy(socks.SOCKS5, "127.0.0.1", 9150)
PROXY_LIST = {"https":"socks5://127.0.0.1:9150"}

class Bot:

    def __init__(self, token):
        self.token = token
        
    def get_incoming(self):
        params = {
            'timeout': 1,
        }
        response = requests.post("https://api.telegram.org/bot%s/getMe" % self.token, params=params, timeout=10, proxies=PROXY_LIST)
        if response.ok:
            print(response)
        

if __name__ == "__main__":
    bot = Bot(os.environ["TASKFU_TOKEN"])
    bot.get_incoming()