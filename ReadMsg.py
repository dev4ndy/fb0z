import SendMsg
import Conexion

class ReadMsg:
    msg = ""
    COMMAND_PEDIR_TEMPERATURA = 1
    sendMsg = None
    stopMsg = 1
    con = None

    def __init__(self, fbChat):
        self.sendMsg = SendMsg.sendMsg(fbChat)

    def setMessage(self, msg):
        self.msg = msg

    def stopMsg(self):
        self.stopMsg = 0

    def decifrarComando(self, msg, code = None):  # En este metodo deberias hacer lo de PLN
        self.con = Conexion.Conexion()
        if msg == "dame la temperatura":
            fltTemperatura = self.con.lectura()
            self.executeAction(SendMsg.sendMsg.ID_MSG_RESPONSE_TEMP, [fltTemperatura])
            self.con.close()
        elif msg == "dame la temperatura en todo momento" or code == 1:
            while self.stopMsg:
                fltTemperatura = self.con.lectura()
                self.executeAction(SendMsg.sendMsg.ID_MSG_RESPONSE_TEMP, [fltTemperatura])
            self.con.close()
            return 1
        elif msg == "parar":
            self.stopMsg = 0
        return 0


    def executeAction(self, comando, datos):
        if comando == self.COMMAND_PEDIR_TEMPERATURA:
            self.sendMsg.send(comando, datos)
