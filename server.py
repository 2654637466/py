# 导入socket模块
from socket import *

# 设置服务器端口号
serverPort = 12000
# 创建一个UDP套接字并绑定到指定端口
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

# 服务器循环接收数据
while True:
    # 接收来自客户端的文件数据和客户端地址
    fileData, clientAddress = serverSocket.recvfrom(2048)
    # 将接收到的文件名解码
    fileName = fileData.decode()

    # 打开文件以二进制写模式
    with open(fileName, 'wb') as file:
        # 持续接收文件数据直到接收到表示文件传输完成的消息
        while True:
            fileChunk, clientAddress = serverSocket.recvfrom(2048)
            if fileChunk == b'FileTransferComplete':
                break
            file.write(fileChunk)

    # 打印接收到的文件名和客户端地址
    print(f"File '{fileName}' received from client {clientAddress}")

#github地址https://github.com/2654637466/py
#在服务器端的代码中，收到的第一个消息是文件名，将其解码后即可获得客户端发送的文件名。
#然后，使用带有'wb'模式的open()函数打开与文件名对应的文件，准备接收数据。没有新建，有覆盖。
#通过循环接收数据块，将每个数据块写入到文件中，直到收到特殊的终止消息"FileTransferComplete"。