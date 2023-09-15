


class Value:

    def __init__(self, token):
        self.value = {}
        if token=='':
            self.value="Null"
            self.type="Null"
        elif token[0]=='#':
            self.type="Boolean"
            if token[1]=='t':
                self.value = True
            elif token[1]=='f':
                self.value = False
        elif token[0] in '0123456789':
            self.type = "Number"
            self.value = int(token)
        elif token[0]=='(':
            self.type="Expression"
            self.inside = token[1:-1]
        elif token[0]=='+':
            self.type="Add"
            self.name="Add"
        elif token[0]=='-':
            self.type="Sub"
            self.name="Sub"
        elif token[0]=='*':
            self.type="Mult"
            self.name="Mult"
        elif type[0]=='/':
            print("MMM")
            self.type="Div"
            self.name="Div"
        else:
            self.type="Idenetifier"

    def __str__(self) -> str:
        return "{"+ "type"+":"+ self.type+  "," +"value"+":" +str( self.value)+ "}" 
