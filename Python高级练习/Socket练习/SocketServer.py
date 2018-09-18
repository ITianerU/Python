#服务器端程序
import socket

def socketServer():
    #AF_INET 是ipv4,SOCK_DGRAM是用UDP
    sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sk.bind(("127.0.0.1",3839))
    #参数是缓存区
    msg,addr = sk.recvfrom(500)
    print(type(msg))
    print(msg.decode())
    #sendto使用udp
    sk.sendto("服务器已连接".encode(),addr)

if __name__ == '__main__':
    print("服务器已开启")
    socketServer()
    print("服务器已关闭")

