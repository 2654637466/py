# 导入socket模块
from socket import *

# 设置服务器的地址和端口号
serverName = '192.168.216.129'
serverPort = 12000

# 创建一个UDP套接字
clientSocket = socket(AF_INET, SOCK_DGRAM)

# 获取用户输入的文件名
fileName = input("Please enter the file name to send: ")

# 将文件名编码并发送到服务器
clientSocket.sendto(fileName.encode(), (serverName, serverPort))

# 打开文件并以二进制模式读取数据
with open(fileName, 'rb') as file:
    # 从文件中读取2048字节的数据
    fileData = file.read(2048)
    # 循环发送文件数据直到文件结束
    while fileData:
        clientSocket.sendto(fileData, (serverName, serverPort))
        fileData = file.read(2048)

# 发送表示文件传输完成的消息
clientSocket.sendto(b'FileTransferComplete', (serverName, serverPort))

# 关闭套接字
clientSocket.close()

#在客户端的代码中，首先要求用户输入要传输的文件名，并将其发送给服务器。
#然后，使用'rb'模式打开待发送的文件。通过循环读取文件数据块，并将每个数据块发送给服务器，直到文件末尾。
#发送完成后，发送特殊的终止消息"FileTransferComplete"以告知服务器传输完成。