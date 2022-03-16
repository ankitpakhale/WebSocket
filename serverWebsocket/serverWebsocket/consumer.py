import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        message = "Hii I'm server"
        self.send(json.dumps({'message': message}))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)

    def disconnect(self, close_code):
        pass

        # message = text_data_json['message']
        # print(f'message come from client {message}')
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))

    # def send(self, text_data=None, bytes_data=None, close=False):
    #     return super().send(text_data, bytes_data, close)()