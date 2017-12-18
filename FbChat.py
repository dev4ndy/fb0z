from fbchat import Client
from fbchat.models import *


class FbChat:
    email = ""
    password = ""
    idChat = ""
    client = None

    def __init__(self, email, password, idChat=None):
        self.email = email
        self.password = password
        self.idChat = idChat
        self.conectar()

    def conectar(self):
        self.client = Client(self.email, self.password)

    def setEmail(self, email):
        self.email = email

    def setIdChat(self, idChat):
        self.idChat = idChat

    def setPassword(self, password):
        self.password = password

    def sendMessageToPerson(self, msg):
        self.client.send(Message(text=msg), thread_id=self.idChat, thread_type=ThreadType.USER)

    def close(self):
        self.client.logout()
