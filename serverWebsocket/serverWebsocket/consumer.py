import json
from channels.generic.websocket import WebsocketConsumer
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        message = 'Message from sever side'
        self.send(json.dumps({'message': message}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(f'message come from client {message}')
        self.send(text_data=json.dumps({
            'message': message
        }))
    # def send(self, text_data=None, bytes_data=None, close=False):
    #     return super().send(text_data, bytes_data, close)()