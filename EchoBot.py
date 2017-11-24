
from fbchat import Client
import ReadMsg
import FbChat
from fbchat import log
from threading import Thread


class EchoBot(Client):
    EMAIL_BOT = "sebas-g9412@hotmail.com"
    PASS_BOT = "94122015402"
    readMsg = None
    fbChat = None
    auxCode = 0
    auxAuthor = None

    def __init__(self, email, password):
        super(EchoBot, self).__init__(email, password)
        self.fbChat = FbChat.FbChat(email, password)
        self.readMsg = ReadMsg.ReadMsg(self.fbChat)

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        # imprimir el log para ver lo que esta pasando.
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # if self.auxCode != 0:
        #   self.fbChat.setIdChat(self.auxAuthor)
        #  self.readMsg.decifrarComando(self.auxCode, self.auxCode)

        if author_id != self.uid:
            self.fbChat.setIdChat(author_id)
            subproceso = Thread(target=self.subproceso, args=(message_object.text,))
            subproceso.start()
            # self.auxCode = self.readMsg.decifrarComando()
           # if self.auxCode != 0:
            #    self.auxAuthor = author_id

    def subproceso(self, msg):
        self.readMsg.decifrarComando(msg)


client = EchoBot(EchoBot.EMAIL_BOT, EchoBot.PASS_BOT)
client.listen()
