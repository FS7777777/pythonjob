from .. import app

class Console():
    '''全局打印类'''
    @staticmethod
    def log(msg):
        if(app.debug):
            print(msg)


    @staticmethod
    def error(msg):
        if(app.debug):
            print(msg)
        
        