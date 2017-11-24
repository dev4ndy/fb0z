import Conexion
import FbChat
import sys

TEMPERATURA_MINIMA = 21.94
TEMPERATURA_MAXIMA = 24.50
con = Conexion.Conexion()
fbChat = FbChat.FbChat('sebas-g9412@hotmail.com', '94122015402', '1116713387')


def enviar(msg):
    fbChat.sendMessageToPerson(msg)

while 1:
    try:
        ftLectura = con.lectura()
        print(ftLectura)
        msg = ""
        if ftLectura <= TEMPERATURA_MINIMA:
            msg = "La temperatura ha desendido hasta: ({}C)".format(str(ftLectura))
        elif ftLectura >= TEMPERATURA_MAXIMA:
            msg = "La temperatura ha aumentado hasta: ({}C)".format(str(ftLectura))

        if msg != "":
            enviar(msg)
    except:
        fbChat.close()  # Cierra la sesion
        con.close()  # Cierra la conexion al arduino
        print("Unexpected error:", sys.exc_info()[0])
        raise
