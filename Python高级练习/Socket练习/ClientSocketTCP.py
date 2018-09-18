#客户端
import socket

def clientSocket():
    cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cs.connect(("127.0.0.1",3839))
    cs.send("尝试连接服务器".encode())
    msg = cs.recv(500)
    print(msg.decode())
    #一定要关闭连接
    cs.close()

if __name__ == '__main__':
    clientSocket()