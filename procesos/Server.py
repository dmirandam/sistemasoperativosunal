import socket
import threading

Bytes = 64
port = 5050  
server = socket.gethostbyname(socket.gethostname()) #ipv4 del dispositivo
print('DIRECCION DEL SERVER: ',server)
adress = (server,port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #configura 'server' como un nuevo socket para ipv4 (AF_INET)<- Family
mensaje_desconeccion='>>DESCONECTADO<<'
server.bind(adress)

def handle(con,dir):
    print(f'Nueva coneccion {dir} conectado')

    conectado = True
    while conectado:
        msg_lng = con.recv(Bytes).decode('utf-8')
        if msg_lng:
            msg_lng = int(msg_lng)
            msg = con.recv(msg_lng).decode('utf-8')
            if msg == mensaje_desconeccion:
                conectado = False
            print(f'[ {dir} ] {msg}')
    con.close()

def star():
    server.listen()
    print('[SERVER ABIERTO]')
    while True:
        con , dir = server.accept()
        new_thread = threading.Thread(target=handle, args=(con,dir))
        new_thread.start()
        print(f'CONEXIONES ACTIVAS ----> {threading.active_count()-1}')

print('[SERVER INICIADO]')
star()