class Test:
    var1 = ""

    def getString(self):
        self.var1 = input()

    def printString(self):
        print(self.var1.upper())


t = Test()
t.getString()
t.printString()
