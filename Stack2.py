class Stack:
    def __init__(self,maxsize) -> None:
        self.maxsize=maxsize
        self.list=[]

    def __str__(self) -> str:
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)

    #is empty

    def isEmpty(self):
        if self.list==[]:
            return True

        else:
            return False

    #is full
    def isFull(self):
        if len(self.list)==self.maxsize:
            return True

        else:
            return False
    
    def push(self,value):
        if self.isFull():
            return "full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "nothing to pop"

        else:
            return self.list.pop()


