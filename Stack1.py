class Stack:
    def __init__(self) -> None:
        self.list=[]
    def __str__(self) -> str:
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)


    #is empty

    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
        return "the element has been successfully inserted"


    def pop(self):
        if self.isempty():
            return "No input"

        else:
            return self.list.pop()

    def peek(self):
        if self.isempty():
            return 'no element'

        else:
            self.list[len(self.list)-1]

    def delete(self):
        self.list=None
customstack=Stack()

customstack.push(3)
customstack.push(4)
customstack.push(1)
customstack.push(0) 
print(customstack)  