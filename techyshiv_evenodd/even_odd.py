class EvenOdd:
    def __init__(self,data) -> None:
        self.data = data
    def checkEven(self):
        typeof=type(self.data)
        if(typeof==int):
            if(self.data % 2 == 0):
                return True
            return False
        elif(typeof==str):
            if(self.data % 2 == 0):
                return True
            return False
        elif(typeof==list):
            even = [i for i in self.data if int(i) % 2 == 0]
            return even
        else:
            return None
    def checkOdd(self):
        typeof=type(self.data)
        if(typeof==int):
            if(self.data % 2 != 0):
                return True
            return False
        elif(typeof==str):
            if(self.data % 2 != 0):
                return True
            return False
        elif(typeof==list):
            odd = [i for i in self.data if int(i) % 2 != 0]
            return odd
        else:
            return None