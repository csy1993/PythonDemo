'''
@Author: CSY
@Date: 2020-03-09 20:45:05
@LastEditors: CSY
@LastEditTime: 2020-03-10 10:14:01
'''
from ftplib import FTP


class FTPTestClient(object):
    """
    FTP客户端
    """

    @staticmethod
    def login(host, user, password, port):
        """
        连接FTP服务器
        :param host: IP地址
        :param user: 用户名
        :param password: 密码
        :param port: 端口
        :return:
        """
        print(host)
        print(user)
        print(password)
        print(port)

        # 实例化客户端对象
        ftp = FTP()

        # 打开调试级别2，显示详细信息
        # ftp.set_debuglevel(2)

        # 设置编码，防止乱码
        ftp.encoding = 'gbk'

        # 连接服务器
        ftp.connect(host, port)

        # 登陆服务器
        ftp.login(user, password)

        # 打印欢迎信息
        print(ftp.getwelcome())
        return ftp

    @staticmethod
    def upload_file(ftp, local, remote):
        """
        上传目标文件
        :param ftp:
        :param local:
        :param remote:
        :return:
        """
        buff_size = 1024
        print(local)
        print(remote)
        uf = open(local, 'rb')
        ftp.storbinary(f"STOR {remote}", uf, buff_size)

    @staticmethod
    def download_file(ftp, remote, local):
        """
        下载目标文件
        :param ftp:
        :param remote:
        :param local:
        :return:
        """
        buff_size = 1024
        print(local)
        print(remote)
        uf = open(local, 'wb')
        ftp.retrbinary(f"RETR {remote}", uf.write, buff_size)


if __name__ == "__main__":
    ftp_client = FTPTestClient()

    host = input("请输入要访问的ftp主机IP地址（默认为localhost）：") or 'localhost'
    port = input("请输入端口号（默认为21）：") or 21
    user = input("请输入用户名：")
    password = input("请输入密码：")

    ftp = ftp_client.login(host, user, password, port)
    # 新建远程目录
    # ftp.mkd("/1")
    # 修改当前目录
    # ftp.cwd("1")
    # 打印目录下文件信息
    # ftp.dir()
    # 获取目录下的文件列表
    # print(ftp.nlst())
    # 获取当前所在位置
    # print(ftp.pwd())

    local = input("请输入要上传的本地文件名：")
    remote = input("请输入远程地址（默认为ftp当前路径）：") or f'./{local}'
    ftp_client.upload_file(ftp, local, remote)

    # 文件更名
    ftp.rename("/FTP.txt", "/FTP2.txt")

    remote = input("请输入要下载的远程文件名：")
    local = input("请输入本地地址（默认为当前路径）：") or f'./{remote}'
    ftp_client.download_file(ftp, remote, local)

    # 删除远程文件
    # ftp.delete("/FTP.txt")
