# coding: utf-8

# 是否开启用户名密码验证
VERIFY = True

# 用户名密码
USER_NAME = 'user'
PASSWORD = '12345'

# 起始目录
DIRECTORY = '/'

PERM = 'elradfmwMT'
# perm权限选项
#
# 读取权限：
# "e" =更改目录（CWD，CDUP命令）
# "l" =列表文件（LIST，NLST，STAT，MLSD，MLST，SIZE命令）
# "r" =从服务器检索文件（RETR命令）
#
# 写入权限：
# "a" =将数据追加到现有文件（APPE命令）
# "d" =删除文件或目录（DELE，RMD命令）
# "f" =重命名文件或目录（RNFR，RNTO命令）
# "m" =创建目录（MKD命令）
# "w" =将文件存储到服务器（STOR，STOU命令）
# "M"=更改文件模式/权限（SITE CHMOD命令）
# "T"=更改文件修改时间（SITE MFMT命令）


# 快速启动
#
# python -m pyftpdlib
# 可选参数
#
# i 指定IP地址（默认为本机的IP地址）
# p 指定端口（默认为2121）
# w 写权限（默认为只读）
# d 指定目录 （默认为当前目录）
# u 指定用户名登录
# P 设置登录密码
