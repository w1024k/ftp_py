# coding=utf-8

'''
pip install pyftpdlib
'''
import sys, commands
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import settings

# 判断是否输入ip
pList = sys.argv
if len(pList) > 1:
    ip = pList[1]
else:
    s = commands.getoutput('hostname -I').strip(' ')
    ip = s.split(' ')[0]

# 实例化DummyAuthorizer来创建ftp用户

authorizer = DummyAuthorizer()

if settings.VERIFY:
    # 参数：用户名，密码，目录，权限
    authorizer.add_user(settings.USER_NAME, settings.PASSWORD, settings.DIRECTORY, settings.PERM)
else:
    # 匿名登录
    authorizer.add_anonymous('/', perm=settings.PERM)
handler = FTPHandler
handler.authorizer = authorizer

# 参数：IP，端口，handler
server = FTPServer(
    (ip, 21),
    handler)

print '%s \n 当前服务地址为: ftp://%s/  \n%s' % ('*' * 50, ip, '*' * 50)
server.serve_forever()
