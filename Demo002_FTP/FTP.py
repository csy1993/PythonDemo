'''
@Author: CSY
@Date: 2020-03-09 20:45:05
@LastEditors: CSY
@LastEditTime: 2020-03-10 10:14:01
'''
from ftplib import FTP
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 搭建FTP服务器
# 实例化DummyAuthorizer来创建ftp用户
authorizer = DummyAuthorizer()
# 参数：用户名，密码，目录，权限
# 读取权限：
# "e" =更改目录（CWD，CDUP命令）
# "l" =列表文件（LIST，NLST，STAT，MLSD，MLST，SIZE命令）
# "r" =从服务器检索文件（RETR命令）
# 写入权限：
# "a" =将数据追加到现有文件（APPE命令）
# "d" =删除文件或目录（DELE，RMD命令）
# "f" =重命名文件或目录（RNFR，RNTO命令）
# "m" =创建目录（MKD命令）
# "w" =将文件存储到服务器（STOR，STOU命令）
# "M"=更改文件模式/权限（SITE CHMOD命令）
# "T"=更改文件修改时间（SITE MFMT命令）
user = input("请输入新建的FTP用户名：")
password = input("请输入新建的FTP用户密码：")
path = input("请输入共享目录（默认为D盘下的share文件夹）：") or r'D:\share'
authorizer.add_user(user, password, path, perm='elradfmwMT')
# 匿名登录
# authorizer.add_anonymous('/home/nobody')
handler = FTPHandler
handler.authorizer = authorizer
# 参数：IP，端口，handler
server = FTPServer(('0.0.0.0', 21), handler)  # 设置为0.0.0.0为本机的IP地址
server.serve_forever()

# 连接FTP服务器
# 实例化客户端对象
ftp = FTP()

# 打开调试级别2，显示详细信息
# ftp.set_debuglevel(2)

# 设置编码，防止乱码
ftp.encoding = 'gbk'

# 连接服务器
host = input("请输入要访问的ftp主机IP地址（默认为localhost）：") or 'localhost'
port = input("请输入端口号（默认为21）：") or 21
ftp.connect(host, port)

# 登陆服务器
user = input("请输入用户名：")
password = input("请输入密码：")
ftp.login(user, password)

print(ftp.getwelcome())  # 打印欢迎信息

ftp.mkd("/1")  # 新建远程目录
ftp.cwd("1")  # 修改当前目录
ftp.dir()  # 打印目录下文件信息
print(ftp.nlst())  # 获取目录下的文件列表
print(ftp.pwd())  # 获取当前所在位置
ftp.rmd("/1")  # 删除远程目录

# 上传目标文件
buff_size = 1024
uf = open("./FTP.txt", 'rb')
ftp.storbinary("STOR /FTP.txt", uf, buff_size)

ftp.rename("/FTP.txt", "/FTP.txt")  # 文件夹更名

# 下载FTP文件
uf = open("FTP.txt", 'wb')
ftp.retrbinary("RETR /FTP.txt", uf.write, buff_size)

ftp.delete("/FTP.txt")  # 删除远程文件
