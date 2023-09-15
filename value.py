


class Value:

    def __init__(self, token):
        if token[0]=='#':
            self.type="Boolean"
            if token[1]=='t':
                self.value = True
            elif token[1]=='f':
                self.value = False
        if token[0] in '0123456789':
            self.type = "Number"
            self.value = int(token)