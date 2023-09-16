


class Value:

    def __init__(self, token):
        pass


    def __str__(self) -> str:
        if self.type=="Expression":
            return "(" + self.inside + ")"
        return "{"+ "type"+":"+ self.type+  "," +"value"+":" +str( self.value)+ "}" 
