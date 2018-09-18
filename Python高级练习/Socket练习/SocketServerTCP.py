#服务器端程序
import socket

def socketServer():
    #AF_INET 是ipv4,SOCK_STREAM是用TCP
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(("127.0.0.1",3839))
    #监听连接
    sk.listen()
    #skt是一个连接
    skt,addr = sk.accept()
    # 参数是缓存区
    msg = skt.recv(500)
    print(msg.decode())
    #send使用tcp
    skt.send("服务器已连接".encode())
    #关闭连接
    skt.close()

if __name__ == '__main__':
    print("服务器已开启")
    socketServer()
    print("服务器已关闭")

