import FbChat


class sendMsg:
    ID_MSG_RESPONSE_TEMP = 1
    ID_MSG_NO_ENTIENDO = 0
    # MSGS es un diccionario, aqui agreguen los mensajes que se desean responder
    MSGS = {
        ID_MSG_RESPONSE_TEMP: "La temperatura es: {} grados",
        ID_MSG_NO_ENTIENDO: "No entiendo..."
    }
    fbChat = None

    def __init__(self, fbChat):
        self.fbChat = fbChat

    def send(self, tipoMsg, datos):
        msg = ""
        if tipoMsg == self.ID_MSG_RESPONSE_TEMP:
            msg = self.MSGS[tipoMsg].format(datos[0])
        # Aquí anidar mas elif de lo que se quiera responder

        if msg != "":
            self.fbChat.sendMessageToPerson(msg)
        else:
            self.fbChat.sendMessageToPerson(self.MSGS[self.ID_MSG_NO_ENTIENDO])
