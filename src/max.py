# coding:utf-8
import urllib
import urllib2
import cookielib
import sys
import re

# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("https://www.python.org/ftp/python/2.7.11/python-2.7.11.msiutf8")
#####################################################
# 登录人人
loginurl = 'http://120.27.145.240/Login/Index'
logindomain = 'renren.com'


class Login(object):

    def __init__(self):
        self.name = ''
        self.passwprd = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def setLoginInfo(self, username, password):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password

    def login(self):
        '''登录网站'''
        loginparams = {'FName': self.name, 'FPwd': self.pwd}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        req = urllib2.Request(loginurl, urllib.urlencode(
            loginparams), headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        print thePage

if __name__ == '__main__':
	userlogin = Login()
	username = 'admin1010'
	password = '11119999'
	userlogin.setLoginInfo(username, password)
	userlogin.login()