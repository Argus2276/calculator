
class Calculator:
    def __init__(self):
        self.AllowedValues = ('+', '-', '*', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '(', ')')
        self.Signs = ('+', '-', '*', '/')
        self.Div = []
    def check(self, *args):
        for arg in args:
            if arg not in self.AllowedValues:
                raise ValueError("Not Allowed Value")
        if args[0] in self.Signs:
            raise ValueError('First Argument must be Number')
        i=0
        while i < len(args):
            if args[i] in self.Signs and args[i+1] in self.Signs:
                raise ValueError("2 sign in a row")
            i+=1
    def divider(self, *args):
        number = ""
        divided = []
        for arg in args:
            if arg.isdigit() or arg == '.':
                number += arg
            else:
                if number != "":
                    divided.append(number)
                    number = ""
                divided.append(arg)
        if number != "":
            divided.append(number)
        self.Div = divided
        return tuple(divided)

    def calculate_in_brackets(self):
        while '(' in self.Div:
            start = None
            for i in range(len(self.Div)):
                if self.Div[i] == '(':
                    start = i
            end = None
            for j in range(start + 1, len(self.Div)):
                if self.Div[j] == ')':
                    end = j
                    break
            inside = self.Div[start + 1: end]
            i = 0
            while i < len(inside):
                if inside[i] == '*':
                    result = float(inside[i - 1]) * float(inside[i + 1])
                    inside[i - 1 : i + 2] = [result]
                    i -= 1
                elif inside[i] == '/':
                    result = float(inside[i - 1]) / float(inside[i + 1])
                    inside[i - 1:i + 2] = [result]
                    i -= 1
                else:
                    i += 1
            i = 0
            while i < len(inside):
                if inside[i] == '+':
                    result = float(inside[i - 1]) + float(inside[i + 1])
                    inside[i - 1:i + 2] = [result]
                    i -= 1
                elif inside[i] == '-':
                    result = float(inside[i - 1]) - float(inside[i + 1])
                    inside[i - 1:i + 2] = [result]
                    i -= 1
                else:
                    i += 1
            self.Div[start: end + 1] = inside

        return self.Div
    def calculate(self):
        i=0
        while i < len(self.Div):
            if self.Div[i] == '*':
                result = float(self.Div[i-1])*float(self.Div[i+1])
                self.Div[i-1:i+2]=[result]
                i-=1
            elif self.Div[i] == '/':
                result = float(self.Div[i-1])/float(self.Div[i+1])
                self.Div[i-1:i+2]=[result]
                i-=1
            else: i+=1
        i=0
        while i < len(self.Div):
            if self.Div[i] == '+':
                result = float(self.Div[i-1])+float(self.Div[i+1])
                self.Div[i-1:i+2]=[result]
                i-=1
            elif self.Div[i] == '-':
                result = float(self.Div[i-1])-float(self.Div[i+1])
                self.Div[i-1:i+2]=[result]
                i-=1
            else: i+=1
        if '.0' in str(self.Div[0]):
            return int(self.Div[0])
        else:
            return self.Div[0]


pr = input()
if len(pr) < 1 or len(pr) > 1000 or "/0" in pr:
    raise ValueError("ERROOO")
obj = Calculator()
obj.check(*pr)
obj.divider(*pr)
obj.calculate_in_brackets()
print(obj.calculate())




