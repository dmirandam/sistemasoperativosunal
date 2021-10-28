from ctypes import string_at
import socket
Bytes = 64
port = 5050 #Este puesrto no esta en uso por el sistema 
mensaje_desconeccion='>>DESCONECTADO<<'
server='192.168.56.1' #Aqui debe estar la direccion del server (Mirar en server.py)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adress = (server,port)
cliente.connect(adress)
a='utf-8'
def send(msg):
    mensaje=msg.encode(a)
    msg_len = len(mensaje)
    ennviar_len = str(msg_len).encode('utf-8')
    ennviar_len += b' '* (Bytes -len(ennviar_len))
    cliente.send(ennviar_len)
    cliente.send(mensaje)


send('Mensaje')
send(mensaje_desconeccion)