from value import Value
from tokenReader import tokenReader

native_env={};

class evaluate1:
    def __init__(self, env=native_env) -> None:
        self.__env__ = native_env

    def eval(self,value):
        pass
    
    def getEnv(self):
        return self.__env__;

if __name__=='__main__':
    pass