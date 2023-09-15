class tokenReader:
    def __init__(self, str):
        self.str = str
        self.start = 0

    def getRest(self):
        return self.str[self.start: ]

    def isEnd(self):
        return self.start>= len(self.str)
    def getNext(self):
        end = self.start
        if self.start<len(self.str) and self.str[self.start] =='(':
            cursor = 1
            end = end+1
            while cursor>0:
                if self.str[end]=='(':
                    cursor=cursor+1
                elif self.str[end]==')':
                    cursor=cursor-1
                end = end+1
            rest = self.str[self.start:end]
            while self.str[end]==' ' and end<len(self.str):
                end = end+1
            self.start = end
            return rest
        else:
            while end < len(self.str) and  (not self.str[end]=='(' and not self.str[end]==' '):
                end = end+1;
            rest = self.str[self.start:end]
            while end < len(self.str) and self.str[end]==' ':
                end = end+1
            self.start = end
            
            return rest.strip();
        


if __name__ == "__main__":
    token= tokenReader("#t #f")
    print(token.getNext())
    print(token.getNext())
