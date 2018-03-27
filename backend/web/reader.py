"""
    使用requests从网络搜集信息，只是为了方便搜集信息而已。
"""
import requests

headers = {  
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",  
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",  
    "Accept-Encoding": "gzip, deflate",  
    "Host": "www.zhihu.com",  
    "Upgrade-Insecure-Requests": "1",  
} 

def login(url):
    """
    处理登录部分
    入参：url
    返回：
    """
    pass

def get_content(page):
    """
    解析page内容
    入参：page

    """
    pass

def write(str):
    """
    写文件读取内容写入文件
    """
    pass

if __name__ == '__main__':
    print('run')