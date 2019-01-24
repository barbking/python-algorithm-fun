# needing to store data in a certain order to access when needed
# stack (LI/FO)

MyStack = []
StackSize = 3

def DisplayStack():
    print("Stack currently contains: ")
    for item in MyStack:
        print(item)

def Push(value):
    if len(MyStack) < StackSize:
        MyStack.append(value)
    else:
        print("Stack is full!")

def Pop():
    if len(MyStack) > 0:
        print("Popping: ", MyStack.pop())
    else:
        print("Stack is empty!")

Push(1)
Push(2)
Push(3)
DisplayStack()
Push(4)

Pop()
DisplayStack()

Pop()
Pop()
Pop()

