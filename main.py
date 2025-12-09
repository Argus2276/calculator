
class Calculator:
    def __init__(self):
        self.allowed_value = ('+', '-', '*', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '(', ')')
        self.signs = ('+', '-', '*', '/')
        self.div = []
    def check(self, *args):
        for arg in args:
            if arg not in self.allowed_value:
                raise ValueError("Not Allowed Value")
        if args[0] in self.signs:
            raise ValueError('First Argument must be Number')
        i=0
        while i < len(args):
            if args[i] in self.signs and args[i+1] in self.signs:
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
        self.div = divided
        return tuple(divided)

    def calculate_in_brackets(self):
        while '(' in self.div:
            start = None
            for i in range(len(self.div)):
                if self.div[i] == '(':
                    start = i
            end = None
            for j in range(start + 1, len(self.div)):
                if self.div[j] == ')':
                    end = j
                    break
            inside = self.div[start + 1: end]
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
            self.div[start: end + 1] = inside

        return self.div
    def calculate(self):
        i=0
        while i < len(self.div):
            if self.div[i] == '*':
                result = float(self.div[i-1])*float(self.div[i+1])
                self.div[i-1:i+2]=[result]
                i-=1
            elif self.div[i] == '/':
                result = float(self.div[i-1])/float(self.div[i+1])
                self.div[i-1:i+2]=[result]
                i-=1
            else: i+=1
        i=0
        while i < len(self.div):
            if self.div[i] == '+':
                result = float(self.div[i-1])+float(self.div[i+1])
                self.div[i-1:i+2]=[result]
                i-=1
            elif self.div[i] == '-':
                result = float(self.div[i-1])-float(self.div[i+1])
                self.div[i-1:i+2]=[result]
                i-=1
            else: i+=1
        if '.0' in str(self.div[0]):
            return int(self.div[0])
        else:
            return self.div[0]


pr = input()
if len(pr) < 1 or len(pr) > 1000 or "/0" in pr:
    raise ValueError("ERROOO")
obj = Calculator()
obj.check(*pr)
obj.divider(*pr)
obj.calculate_in_brackets
print(obj.calculate())





