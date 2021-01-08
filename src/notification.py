import requests


class Notification:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        self.get_result = None

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        self.get_result = resp.json()['result']

    def send(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        if len(self.get_result) > 0:
            return self.get_result[-1]

    def send_n(self, name, phone):
        self.send(chat_id=296438055, text='Новая заявка: ' + phone + ', ' + name)