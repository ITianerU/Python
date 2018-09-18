#客户端
import socket

def clientSocket():
    cs = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    cs.sendto("尝试连接服务器".encode(),("127.0.0.1",3839))
    msg,addr = cs.recvfrom(500)
    print(msg.decode())

if __name__ == '__main__':
    clientSocket()